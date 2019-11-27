from .controller.app import resolve
from .core.app import play
import sys

if __name__ == 'main':
    if sys.argv[0] == 'play':
        play()
    else:
        print(resolve(sys.argv))