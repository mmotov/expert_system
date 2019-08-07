
colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'pink': '\033[95m',
    'end_color': '\033[0m',
}


def red(string):
    return colors['red'] + string + colors['end_color']


def yellow(string):
    return colors['yellow'] + string + colors['end_color']


def green(string):
    return colors['green'] + string + colors['end_color']


def blue(string):
    return colors['blue'] + string + colors['end_color']


def pink(string):
    return colors['pink'] + string + colors['end_color']