import sys
from client import definitions, synonyms, antonyms, all_results, random_word, examples
<<<<<<< HEAD
from core import play, print_pretty, _common
=======
from core import play, print_pretty
>>>>>>> 97716f3498f035286d9dafaa544ade3f7028a795

# this map should be open for extension and closed for modifications
_ops_map = {
    'defn': definitions,
    'syn': synonyms,
    'ant': antonyms,
    'ex': examples
}

_max_arguments = 3  # 2+1 (filename.py)


# routing logic
def resolve(args):
    print("Getting info for you...")
    # first argument is 'filename.py'
    if len(args) > _max_arguments:
        print ('Invalid Input')
    elif len(args) == _max_arguments:
        if args[1] not in _ops_map:
            print(f'invalid operation: {args[1]}')
        else:
            return _ops_map[args[1]](args[2])
    elif len(args) == 2:
        return all_results(args[1])
    elif len(args) == 1:
        return all_results(random_word())


if __name__ == '__main__':
    if sys.argv[1] == 'play':
        play()
    else:
        print_pretty(resolve(sys.argv))
