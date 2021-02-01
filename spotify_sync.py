
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from time import sleep

from .colors.colors import adjust_color, get_album_colors,rgb2hsv,hsv2rgb
from .modules.razer_chroma.aud_razer import  RazerAudioVisualizer
from .modules.razer_chroma.razer_chroma import RazerController

from .modules.ambient.ambient import Ambient

from .modules.rgb_keyboard.keyboard_matrix import KeyboardMatrix
from .modules.rgb_keyboard.keyboard_controller import KeyboardHIDController
from .modules.rgb_keyboard.aud_keyboard import KeyboardAudioVisualizer

from .modules.rgb_ecio.rgb_ecio import ECIOController
from .modules.rgb_ecio.aud_ecio import ECIOAudioVisualizer

from .shared_audio import SharedAudioController

from .config import *
import asyncio

import allogate as logging

auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            scope="user-read-playback-state",
                            redirect_uri="http://127.0.0.1:5001/")

#complete oauth
sp = spotipy.Spotify(auth_manager=auth_manager)


# wait until song changes
async def song_changed(last):
    song=last
    while song["item"]["external_urls"]["spotify"]==last["item"]["external_urls"]["spotify"]:
        
        song = await get_song()
        #wait for next poll if song didn't change
        if(not song):
            await asyncio.sleep(SPOTIFY_POLL_INTERVAL*3)
        if(song["item"]["external_urls"]["spotify"]!=last["item"]["external_urls"]["spotify"]): 
            return song
        await asyncio.sleep(SPOTIFY_POLL_INTERVAL)

# get current song that is playing
async def get_song():
    song = sp.currently_playing()
    if(song):
        s = song["item"]["external_urls"]["spotify"]
        logging.pprint(f'song is : {s}', 4)
    return song


async def main(loop):
    last = ""
    
    logging.VERBOSITY = VERBOSITY
    
    # check if a song is playing, wait until it starts
    song = None
    while not song:
        song = await get_song()

    last = song

    audio_controller = SharedAudioController(dampen=AUDIO_DAMPEN)
    #get palette from album
    r,g,b = await get_album_colors(song)
    r,g,b = adjust_color(r,g,b,OVERSATURATE_ALBUM_PALLETTE, OVEREXPOSE_ALBUM_PALLETTE)
    
    logging.pprint(f'Pallette is set to {r},{g},{b}', 3)

    razer_vis = None
    keyboard_vis = None
    ecio_vis = None
    ambient_colors = None

    # create and set razer controller device from razer-pychroma
    if(DO_RAZER):
        razer_controller = RazerController()
        razer_vis = RazerAudioVisualizer(razer_controller, audio_controller, fade=RAZER_FADE, delay=RAZER_VISUALS_INTERVAL, dampen=RAZER_DAMPEN, ceiling=RAZER_CEILING, ambient_brightness_coef=RAZER_AMBIENT)
        await razer_vis.change_color(r,g,b)
        loop.create_task(razer_vis.visualize())

    # create and set rgb keyboard controller (not razer) from FlameOfIgnis/rgb_keyboard
    if(DO_KEYBOARD):
        keybd_controller = KeyboardHIDController()
        keyboard_matrix  = KeyboardMatrix(keybd_controller)
        keyboard_vis = KeyboardAudioVisualizer(keyboard_matrix, audio_controller, fade=KEYBOARD_FADE, delay=KEYBOARD_VISUALS_INTERVAL, dampen=KEYBOARD_DAMPEN, ceiling=KEYBOARD_CEILING, ambient_brightness_coef=KEYBOARD_AMBIENT, dampen_bias=KEYBOARD_DAMPEN_BIAS, ceiling_bias=KEYBOARD_CEILING_BIAS)
        await keyboard_vis.change_color(r,g,b)
        loop.create_task(keyboard_vis.visualize())
    
    # create and set ECIO strip controller from FlameOfIgnis/ecio_rgb
    if(DO_ECIO):
        ecio_controller = ECIOController()
        ecio_vis = ECIOAudioVisualizer(ecio_controller, audio_controller, fade=ECIO_FADE, delay=ECIO_VISUALS_INTERVAL, dampen=ECIO_DAMPEN, ceiling=ECIO_CEILING, ambient_brightness_coef=ECIO_AMBIENT)
        await ecio_vis.change_color(r,g,b)
        loop.create_task(ecio_vis.visualize())
    
    if(DO_BACKGROUND):
        ambient_colors = Ambient()
        ambient_colors.change_color(r,g,b)

    loop.create_task(audio_controller.refresh_loop())
    while True:
        song = await song_changed(last);
        last=song
        logging.pprint(f"Now playing: {song['item']['name']} by {song['item']['album']['artists'][0]['name']}.", 1)
        #image to rgb elements
        r,g,b = await get_album_colors(song)
        r,g,b = adjust_color(r,g,b,OVERSATURATE_ALBUM_PALLETTE, OVEREXPOSE_ALBUM_PALLETTE)
        
        if(DO_KEYBOARD):
            loop.create_task(keyboard_vis.change_color(r,g,b))

        if(DO_ECIO):
            loop.create_task(ecio_vis.change_color(r,g,b))
        
        if(DO_BACKGROUND):
            ambient_colors.change_color(r,g,b)
        
        if(DO_RAZER):
            loop.create_task(razer_vis.change_color(r,g,b))
        
