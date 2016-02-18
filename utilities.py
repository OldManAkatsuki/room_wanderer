import textwrap
from textwrap import TextWrapper
from colorama import init
from blessings import Terminal


init(autoreset=True)  # initialize colorama wrapping
term = Terminal()


def gprint_format(text, indent):
    spaces = '     ' * indent
    t = TextWrapper(width=70)
    return textwrap.indent(t.fill(text), spaces)


def gprint(text, color=None, indent=1):
    if color:
        color_code = getattr(term, color, '')
        print(gprint_format('{}{}{t.normal}'.format(color_code, text, t=term), indent=indent))
    else:
        print(gprint_format(text, indent=indent))


def gprint_colorize(text, color):
    color_code = getattr(term, color, '')
    return '{}{}{t.normal}'.format(color_code, text, t=term)
