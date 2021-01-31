from PIL import Image
import requests
import urllib.request
import asyncio 
import aiohttp
import aiofiles
import colorsys
import os.path

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
    
def rgb2hsv(r,g,b):
    return colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

def get_colors(image_file, numcolors=10, resize=150):
    # Resize image to speed up processing
    img = Image.open(image_file)
    img = img.copy()
    img.thumbnail((resize, resize))

    # Reduce to palette
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=1)

    # Find dominant colors
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    colors = list()
    for i in range(numcolors):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        colors.append(tuple(dominant_color))
    return colors

async def get_album_colors(song):
    #get album thumbnail
    filename = song.split('/')[-1]
    directory = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '.albums', filename))
    #check from cache first
    if os.path.exists(directory):
        return get_colors(directory, numcolors=1)[0]

    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        params = {'url': song}
        async with session.get("https://open.spotify.com/oembed", params=params, headers=headers) as response:
            async with session.get((await response.json())["thumbnail_url"], params=params, headers=headers) as resp:
                f = await aiofiles.open(directory, mode='wb')
                await f.write(await resp.read())
                await f.close()
    #image_url = requests.get().json()["thumbnail_url"]
    #urllib.request.urlretrieve(image_url, "cover.png")

    #image to rgb elements
    return get_colors(directory, numcolors=1)[0]


    