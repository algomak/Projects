from controller.app import resolve
from core import play, print_pretty
import sys
from requests import HTTPError


def main():
    try:
        if sys.argv[1] == 'play':
            play()
        else:
            print_pretty(resolve(sys.argv))
    except HTTPError as exc:
        print(f"HTTPError: {exc.response.status_code}, {exc.response.text}")
    except Exception as exc:
        print(f"Unknown exception occurred!: {exc}")