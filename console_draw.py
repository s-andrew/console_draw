# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:14:32 2018

@author: AnSo
"""

from PIL import Image
from colorama import Back, Fore, init

draw = lambda b, f, s: print(b + f + s, end='')

def quantizetopalette(silf, palette):
    silf.load()
    palette.load()
    im = silf.im.convert("P", 0, palette.im)
    return silf._new(im)


palimage  = Image.new('P', (16, 16))
palettedata = [ 0, 0, 0, 255, 0, 0, 255, 255, 0, 0, 255, 0, 255, 255, 255,85,255,85, 255,85,85, 255,255,85]
palimage.putpalette(palettedata * 32)


color_draw = dict()
color_draw[0] = lambda s: draw(Back.BLACK, Fore.BLACK, s)
color_draw[1] = lambda s: draw(Back.RED, Fore.RED, s)
color_draw[2] = lambda s: draw(Back.LIGHTYELLOW_EX, Fore.LIGHTYELLOW_EX, s)
color_draw[3] = lambda s: draw(Back.GREEN, Fore.GREEN, s)
color_draw[4] = lambda s: draw(Back.WHITE, Fore.WHITE, s)
color_draw[5] = lambda s: draw(Back.LIGHTGREEN_EX, Fore.LIGHTGREEN_EX, s)
color_draw[6] = lambda s: draw(Back.YELLOW, Fore.YELLOW, s)
color_draw[7] = lambda s: draw(Back.YELLOW, Fore.BLACK, s)
#color_draw[7] = lambda s: draw(Back.LIGHTYELLOW_EX, Fore.LIGHTYELLOW_EX, s)
n = lambda: draw(Back.RESET, Fore.RESET, '\n')


printimage = quantizetopalette(Image.open('pixels.png'), palimage)
width, height = printimage.size
printpixel = printimage.load()
init()
for j in range(height):
    for i in range(width):
        color = printpixel[i, j]
        color_draw[color]('.')
    n()