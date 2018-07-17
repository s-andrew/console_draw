from itertools import repeat, starmap

from PIL import Image
import numpy as np
from colorama import Back, Fore, init

from alphabet import ALPHABET, SPACE

init()
CONSOLE_COLORS = {
        0: (Back.BLACK, Fore.BLACK),
        1: (Back.RED, Fore.RED),
        2: (Back.YELLOW, Fore.YELLOW),
        3: (Back.GREEN, Fore.GREEN),
        4: (Back.WHITE, Fore.WHITE),
        5: (Back.LIGHTGREEN_EX, Fore.LIGHTGREEN_EX),
        6: (Back.LIGHTYELLOW_EX, Fore.LIGHTYELLOW_EX),
        7: (Back.LIGHTYELLOW_EX, Fore.YELLOW),
        'n': (Back.RESET, Fore.RESET)
        }


def pixel_mapper(color, fill):
    back, fore = CONSOLE_COLORS[color]
    return back + fore + fill


def join(l, sep):
    newl = [sep]
    for i in l:
        newl.append(i)
        newl.append(sep)
    return newl

def newline():
    return pixel_mapper('n', '\n')


def string2matrix(string, font_color, back_color, interligne):
    string = string.lower()
    matrixes = map(lambda x: ALPHABET[x], string)
    matrix = join(matrixes, SPACE)
    matrix = np.concatenate(matrix, axis=1)
    _, w = matrix.shape
    line_space = np.zeros((interligne, w))
    matrix = np.concatenate([line_space, matrix, line_space], axis=0)
    colorize = lambda x: font_color if x else back_color
    mapper = lambda x: np.array(list(map(colorize, x)))
    matrix = np.apply_along_axis(mapper, axis=0, arr=matrix)
    return matrix


def matrix2printable(matrix, fill_symbol):
    for row in matrix:
        row = starmap(pixel_mapper, zip(row, repeat(fill_symbol)))
        row = ''.join(row)
        yield row


def draw_string(string, font_color=4, back_color=0, fill_symbol='.', interligne=1):
    matrix = string2matrix(string, font_color, back_color, interligne)
    print(*list(matrix2printable(matrix, fill_symbol)), sep=newline())
    return


def quantizetopalette(silf, palette):
    silf.load()
    palette.load()
    im = silf.im.convert("P", 0, palette.im)
    return silf._new(im)


def open_image(file_name):
    palimage  = Image.new('P', (16, 16))
    palettedata = [ 0, 0, 0, 255, 0, 0, 255, 255, 0, 0, 255, 0, 255, 255, 255,85,255,85, 255,85,85, 255,255,85]
    palimage.putpalette(palettedata * 32)
    return np.array(quantizetopalette(Image.open(file_name), palimage))


def draw_image(file_name, fill_sym='.'):
    matrix = open_image(file_name)
    print(*list(matrix2printable(matrix, '.')), sep=newline())
    return
    







