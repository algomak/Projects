import sys
from ..client import definations, synonyms, antonyms, all_results, random_word, examples
from ..core import play

# this map should be open for extension and closed for modifications
_ops_map = {
    'defn': definations,
    'syn': synonyms,
    'ant': antonyms,
    'ex': examples
}


# routing logic
def resolve(args):
    if len(args) > 2:
        return 'Invalid Input'
    elif len(args) == 2:
        if args[0] not in _ops_map:
            return 'invalid operation'
        else:
            _ops_map[args[0]](args[1])
    elif len(args) == 1:
        all_results(args[0])
    elif len(args) == 0:
        all_results(random_word())


if __name__ == 'main':
    if sys.argv[0] == 'play':
        play()
    else:
        print(resolve(sys.argv))
