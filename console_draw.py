from PIL import Image
import numpy as np
from colorama import Back, Fore, init

from alphabet import ALPHABET, SPACE

init()


def draw(back, fore, symbol):
    print(back + fore + symbol, end='')
    return


def draw_pixel(color, symbol):
    color_draw = dict()
    color_draw[0] = lambda s: draw(Back.BLACK, Fore.BLACK, s)
    color_draw[1] = lambda s: draw(Back.RED, Fore.RED, s)
    color_draw[2] = lambda s: draw(Back.YELLOW, Fore.YELLOW, s)
    color_draw[3] = lambda s: draw(Back.GREEN, Fore.GREEN, s)
    color_draw[4] = lambda s: draw(Back.WHITE, Fore.WHITE, s)
    color_draw[5] = lambda s: draw(Back.LIGHTGREEN_EX, Fore.LIGHTGREEN_EX, s)
    color_draw[6] = lambda s: draw(Back.LIGHTYELLOW_EX, Fore.LIGHTYELLOW_EX, s)
    color_draw[7] = lambda s: draw(Back.LIGHTYELLOW_EX, Fore.YELLOW, s)
#    color_draw[0] = lambda s: draw(Back.BLACK, Fore.BLACK, s)
#    color_draw[1] = lambda s: draw(Back.RED, Fore.RED, s)
#    color_draw[2] = lambda s: draw(Back.YELLOW, Fore.LIGHTYELLOW_EX, s)
#    color_draw[3] = lambda s: draw(Back.GREEN, Fore.GREEN, s)
#    color_draw[4] = lambda s: draw(Back.WHITE, Fore.WHITE, s)
#    color_draw[5] = lambda s: draw(Back.LIGHTGREEN_EX, Fore.LIGHTGREEN_EX, s)
#    color_draw[6] = lambda s: draw(Back.YELLOW, Fore.YELLOW, s)
#    color_draw[7] = lambda s: draw(Back.LIGHTYELLOW_EX, Fore.BLACK, s)
    color_draw[color](symbol)
    return


def newline():
    draw(Back.RESET, Fore.RESET, '\n')
    return


def join(l, sep):
    newl = [sep]
    for i in l:
        newl.append(i)
        newl.append(sep)
    return newl


def draw_string(s, font_color=4, back_color=0, fill_symbol='.'):
    s = s.lower()
    s = map(lambda x: ALPHABET[x], s)
    s = join(s, SPACE)
    s = np.concatenate(s, axis=1)
    for row in s:
        for sym in row:
            color = font_color if sym else back_color
            draw_pixel(color, fill_symbol)
        newline()
    return


def quantizetopalette(silf, palette):
    silf.load()
    palette.load()
    im = silf.im.convert("P", 0, palette.im)
    return silf._new(im)


def draw_image(file_name, fill_sym='.'):
    palimage  = Image.new('P', (16, 16))
    palettedata = [ 0, 0, 0, 255, 0, 0, 255, 255, 0, 0, 255, 0, 255, 255, 255,85,255,85, 255,85,85, 255,255,85]
#    palettedata = [ 0, 0, 0, 85,255,255, 255,85,85, 255,255,255]
    palimage.putpalette(palettedata * 32)

    printimage = quantizetopalette(Image.open(file_name), palimage)
    width, height = printimage.size
    printpixel = printimage.load()
    init()
    for j in range(height):
        for i in range(width):
            color = printpixel[i, j]
            draw_pixel(color, fill_sym)
        newline()
    return printimage
    

