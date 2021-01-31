
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from time import sleep

from .colors.colors import get_album_colors,rgb2hsv,hsv2rgb
from .modules.razer_chroma.aud_razer import  RazerAudioVisualizer
from .modules.razer_chroma.razer_chroma import RazerController

from .modules.ambient.ambient import change_ambient

from .modules.rgb_keyboard.keyboard_matrix import KeyboardMatrix
from .modules.rgb_keyboard.keyboard_controller import KeyboardHIDController
from .modules.rgb_keyboard.aud_keyboard import KeyboardAudioVisualizer

from .modules.rgb_ecio.rgb_ecio import ECIOController
from .modules.rgb_ecio.aud_ecio import ECIOAudioVisualizer

from .modules.rgb_keyboard.audio_loopback.audio_loopback import AudioController

from .config import *
import asyncio

import allogate as logging

auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            scope="user-read-playback-state",
                            redirect_uri="http://127.0.0.1:5001/")

#complete oauth
sp = spotipy.Spotify(auth_manager=auth_manager)


async def song_changed(last):
    song=last
    while song==last:
        
        song = await get_song()
        #wait for next poll if song didn't change
        if(song!=last): 
            return song
        await asyncio.sleep(SPOTIFY_POLL_INTERVAL)

async def get_song():
    s = sp.currently_playing()["item"]["external_urls"]["spotify"]
    logging.pprint(f'song is : {s}', 4)
    return s


async def main(loop):
    last = ""
    
    logging.VERBOSITY = VERBOSITY
    
    #poll and wait until song changes
    song = await get_song()
    
    audio_controller = AudioController(dampen=5)
    #get palette from album
    r,g,b = await get_album_colors(song)
    
    #rgb -> hsv, then hsv->rgb with full saturation
    if(OVERSATURATE_ALBUM_PALLETTE):
        h,s,v = rgb2hsv(r,g,b)
        r,g,b = hsv2rgb(h,1,v)
    
    logging.pprint(f'Pallette is set to {r},{g},{b}', 3)

    razer_vis = None
    keyboard_vis = None
    if(DO_RAZER):
        razer_controller = RazerController()
        razer_vis = RazerAudioVisualizer(razer_controller, audio_controller)
        await razer_vis.change_color(r,g,b)
        loop.create_task(razer_vis.visualize())

    if(DO_KEYBOARD):
        keybd_controller = KeyboardHIDController()
        keyboard_matrix  = KeyboardMatrix(keybd_controller)
        keyboard_vis = KeyboardAudioVisualizer(keyboard_matrix, audio_controller )
        await keyboard_vis.change_color(r,g,b)
        loop.create_task(keyboard_vis.visualize())
    
    ecio_controller = ECIOController()
    ecio_vis = ECIOAudioVisualizer(ecio_controller, audio_controller)
    await keyboard_vis.change_color(r,g,b)
    loop.create_task(ecio_vis.visualize())
    
    while True:
        song = await song_changed(last);
        last=song
        logging.pprint(f"now playing: {song}", 1)
        #image to rgb elements
        r,g,b = await get_album_colors(song)
        if(OVERSATURATE_ALBUM_PALLETTE):
            h,s,v = rgb2hsv(r,g,b)
            r,g,b = hsv2rgb(h,1,v)
        
        if(DO_KEYBOARD):
            await keyboard_vis.change_color(r,g,b)
            await ecio_vis.change_color(r,g,b)
        
        # change desktop background to flat
        if(DO_BACKGROUND):
            ambient = "%02x%02x%02x" % (b,g,r)
            logging.pprint(f"Ambient colors: {ambient}", 2)
            change_ambient(ambient)
        if(DO_RAZER):
            loop.create_task(razer_vis.change_color(r,g,b))
        
