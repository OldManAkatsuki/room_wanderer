import textwrap
from textwrap import TextWrapper
# from colorama import init
# from blessings import Terminal


# init(autoreset=True)  # initialize colorama wrapping
# term = Terminal()


def gprint_format(text):
    t = TextWrapper(width=70)
    return textwrap.indent(t.fill(text), '     ')


def gprint(text, color=None):
    # if color:
    #     color_code = getattr(term, color, '')
    #     print(gprint_format('{}{}{t.normal}'.format(color_code, text, t=term)))
    # else:
    print(gprint_format(text))
