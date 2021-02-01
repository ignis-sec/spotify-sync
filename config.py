
#spotify oauth key, from https://developer.spotify.com/dashboard/applications
client_id="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Do keyboard equalizer animations
DO_KEYBOARD=True

# Do razer device animations
DO_RAZER=True

# Change desktop background color with the song
DO_BACKGROUND=False

# ECIO device colors, most devices might not have these built in led strips
DO_ECIO = False

# If set, will attempt to oversaturate colors to make prettier
OVERSATURATE_ALBUM_PALLETTE=True

# If set, will attempt to overexpose the colors, making them brighter
# If one of your devices has bad color calibration, this is just going to make it worse though
OVEREXPOSE_ALBUM_PALLETTE=False


#how often to poll spotify for song changes (s)
SPOTIFY_POLL_INTERVAL = 1

#global verbosity
VERBOSITY = 3

# Only use if your audio levels are hitting the ceiling/getting flat colors
AUDIO_DAMPEN = 5



#################################### Razer Mouse / Headset config ####################################

# Higher the value, longer it will take for a color to "discharge"
RAZER_FADE = 0.8

# slows down animation framerate
RAZER_VISUALS_INTERVAL = 0

# Dampen audio values after preprocessing, and after FFT. 
# Deprecated, AUDIO_DAMPEN should do the trick (dampen audio before after fft, before preprocessing)
RAZER_DAMPEN = 0

# Audio value that will be mapped to maximum brightness
RAZER_CEILING = 180

# coefficient for minimum brightess (so device doesn't turn off when there is no audio, just dims down)
RAZER_AMBIENT = 0.1



#################################### Razer Mouse / Headset config ####################################

# Higher the value, longer it will take for a color to "discharge"
ECIO_FADE = 0.8
 
# slows down animation framerate
ECIO_VISUALS_INTERVAL = 0

# Dampen audio values after preprocessing, and after FFT. 
# Deprecated, AUDIO_DAMPEN should do the trick (dampen audio before after fft, before preprocessing)
ECIO_DAMPEN = 0

# Audio value that will be mapped to maximum brightness
ECIO_CEILING = 180

# coefficient for minimum brightess (so device doesn't turn off when there is no audio, just dims down)
ECIO_AMBIENT = 0.25



#################################### Razer Mouse / Headset config ####################################

# Higher the value, longer it will take for a color to "discharge"
KEYBOARD_FADE = 0.8

# slows down animation framerate
KEYBOARD_VISUALS_INTERVAL = 0

# Dampen audio values after preprocessing, and after FFT. 
# Deprecated, AUDIO_DAMPEN should do the trick (dampen audio before after fft, before preprocessing)
KEYBOARD_DAMPEN = 0

# Audio value that will be mapped to maximum brightness
KEYBOARD_CEILING = 120

# work in progress
KEYBOARD_AMBIENT = 0.001

# Dampening coefficient for each column of keyboard, so adjustments can be made for higher pitches
KEYBOARD_DAMPEN_BIAS = 0.98

# Ceiling coefficient for each column of keyboard, so adjustments can be made for higher pitches
KEYBOARD_CEILING_BIAS = 0.985