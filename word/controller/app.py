import sys
from client import definations, synonyms, antonyms, all_results, random_word, examples
from core import play

# this map should be open for extension and closed for modifications
_ops_map = {
    'defn': definations,
    'syn': synonyms,
    'ant': antonyms,
    'ex': examples
}

_max_arguments = 3 # 2+1 (filename.py)

# routing logic
def resolve(args):
    # first argument is 'filename.py'
    if len(args) > _max_arguments:
        return 'Invalid Input'
    elif len(args) == _max_arguments:
        if args[1] not in _ops_map:
            return 'invalid operation'
        else:
            _ops_map[args[1]](args[2])
    elif len(args) == 2:
        all_results(args[1])
    elif len(args) == 1:
        all_results(random_word())


if __name__ == 'main':
    if sys.argv[0] == 'play':
        play()
    else:
        print(resolve(sys.argv))
