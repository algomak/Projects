from controller.app import resolve
from core import play, print_pretty
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'play':
        play()
    else:
        res = resolve(sys.argv)
        print_pretty(res)