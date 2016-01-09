import textwrap
from textwrap import TextWrapper
from colorama import init
from blessings import Terminal


init(autoreset=True)  # initialize colorama wrapping
term = Terminal()


def gprint_format(text):
    t = TextWrapper(width=70, expand_tabs=True, tabsize=4)
    return textwrap.indent(t.fill(text), '     ')


def gprint(text):
    print(gprint_format(text))


def gprint_color(text, color=None):
    if color:
        color_code = getattr(term, color, '')
        gprint('{}{}{t.normal}'.format(color_code, text, t=term))
    else:
        gprint(text)
