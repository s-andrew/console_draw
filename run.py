import argparse

from console_draw import draw_string, draw_image


main_parser = argparse.ArgumentParser()
main_parser.add_argument('-i', '--image', type=str, help='Path to image', dest='params', action='append')
main_parser.add_argument('-t', '--text', type=str, help='Text to print', dest='params', action='append')
main_parser.add_argument('--fill-sym', type=str, help='Fill symbol', default=' ')

support_parser = argparse.ArgumentParser(
    add_help=False, parents=[main_parser], conflict_handler='resolve',
    description='For example: python run.py -i img/crash.png -t "         Let\'s crash this party!" --fill-sym "  "'

)
support_parser.add_argument('-i', '--image', help='Path to image', dest='images', action='append')
support_parser.add_argument('-t', '--text', help='Text to print', dest='texts', action='append')


types = support_parser.parse_args()
main = main_parser.parse_args()
report = []

for v in main.params:
    if types.images is not None and v in types.images:
        try:
            draw_image(v, fill_sym=main.fill_sym)
        except FileNotFoundError:
            report.append("No such file or directory: '%s'"%v)
    if types.texts is not None and v in types.texts:
            draw_string(v, fill_symbol=main.fill_sym)


for i in report:
    print(i)


print(main.fill_sym)


# from itertools import chain
# s = '''\
# Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
# tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
# consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
# cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
# proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\
# '''
# s = s.replace('\n', '')
# l = s.split('.')
# l = map(lambda x: x + '.', l)
#
# l = map(lambda x: x.split(','), l)
#
# rows = []
# for phrase in l:
#     *body, last = phrase
#     body = map(lambda x: x + ',', body)
#     phrase = list(body) + [last]
#     rows += phrase
#
# for row in rows:
#     draw_string(row)
    
    


