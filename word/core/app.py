import logging
import random

from ._common import _get_user_input, _get_another_randomly, _choices_list, print_pretty
import client  # circular import
<<<<<<< HEAD
from ._common import _word_structure
=======
>>>>>>> 97716f3498f035286d9dafaa544ade3f7028a795

log = logging.getLogger(__name__)


def _setup_game_word(word):
    game_word = {
        'word': word,
        'defn': None,
        'syn': None,
        'ant': None
    }
    random_relation = 'syn'
    if (word.syn and word.ant) and \
        len(word.syn) and len(word.ant):
        random_relation = random.choice(['syn', 'ant'])
    game_word[random_relation] = _get_another_randomly(word, random_relation)
    game_word['defn'] = _get_another_randomly(word, 'defn')
    log.info(f'generated game word: {str(game_word)}')
<<<<<<< HEAD
    # print info to user
    for key in game_word:
        if key != 'word' and game_word[key] is not None:
            print(
                f"{_word_structure[key]}: {game_word[key]}"
            )
=======
>>>>>>> 97716f3498f035286d9dafaa544ade3f7028a795
    return game_word


def _show_wrong_word_interface():
    print("Wrong Word! select one of below choices")
    while True:
        print_pretty(_choices_list)
        user_input = _get_user_input("Enter your choice: ")
        if user_input in _wrong_interface_map:
            return user_input
        else:
            print("Wrong choice try again!")


# find out better design where unnecessary param "game_word" should not be sent
def _try_again(game_word):
    return _get_user_input("Guess the word: "), False


def _hint(game_word):
    """

    :param word:
    :param curr_syn_or_ant:
    :return:
    randomly selects one of these:
            1. Display the word randomly jumbled (cat => atc, tac, tca)
            2. Display another definition of the word
            3. Display another antonym of the word
            4. Display another synonym of the word
    """

    print("Hint: ")
    print('\n'.join([f'{k}: {_hint_print_tuple[k]}' for k in _hint_print_tuple]))
    user_input = _get_user_input()
    while user_input not in _hint_print_tuple:
        print("Wrong choice, try again!")
        print('\n'.join([f'{k}: {_hint_print_tuple[k]}' for k in _hint_print_tuple]))
        user_input = _get_user_input()
    _hint_interface_map[user_input](game_word)
    return _try_again(game_word)


def _quit(game_word):
    print(f"Correct answer is: ")
    print_pretty(game_word['word'])
    print("Better luck next time!")
    return '', True


def _jumble_word(game_word) -> str:
    word = game_word['word']
    word_list = list(word.literal_value)
    random.shuffle(word_list)
    print(f"jumbled word is: {''.join(word_list)}")


def _another_defn(game_word) -> None:
    log.info("Getting another definition")
    result = _get_another_randomly(game_word['word'], 'defn', game_word['defn'])
    if result is not None:
        print(f"Another definition: {result}")
    else:
        print("Sorry! I don't have any more definitions of this word!")


def _another_syn(game_word) -> None:
    log.info("Getting another synonym")
    result = _get_another_randomly(game_word['word'], 'syn', game_word['syn'])
    if result is not None:
        print(f"Another synonym: {result}")
    else:
        print("Sorry! I don't have any more synonyms of this word!")


def _another_ant(game_word) -> None:
    log.info("Getting another antonym")
    result = _get_another_randomly(game_word['word'], 'ant', game_word['ant'])
    if result is not None:
        print(f"Another antonym: {_get_another_randomly(game_word['word'], 'ant', game_word['ant'])}")
    else:
        print("Sorry! I don't have any more antonyms of this word!")


_wrong_interface_map = {
    '1': _try_again,
    '2': _hint,
    '3': _quit
}

_hint_interface_map = {
    '1': _jumble_word,
    '2': _another_defn,
    '3': _another_syn,
    '4': _another_ant
}

_hint_print_tuple = {
    '1': "Display the word randomly jumbled (cat => atc, tac, tca)",
    '2': "Display another definition of the word",
<<<<<<< HEAD
    '3': "Display another synonym of the word",
    '4': "Display another antonym of the word"
=======
    '3': "Display another antonym of the word",
    '4': "Display another synonym of the word"
>>>>>>> 97716f3498f035286d9dafaa544ade3f7028a795
}


def play(word=None):
    print("Preparing game environment...")
    """

    :param word:
    :return:
    """
    if word is None:
        word = client.all_results()
    game_word = _setup_game_word(word)
    # as choice of getting synonym or antonym is random we will check here
    # 1. get user input
    user_word = _get_user_input()
    end_game = False
    while not end_game:
        # keep playing
        if user_word == word.literal_value or user_word in word.syn:
<<<<<<< HEAD
            print('Correct answer! You won!')
            return
        user_input = _show_wrong_word_interface()
        user_word, end_game = _wrong_interface_map[user_input](game_word)
    return
=======
            return 'Correct answer! You won!'
        user_input = _show_wrong_word_interface()
        user_word, end_game = _wrong_interface_map[user_input](game_word)
    return "Better luck next time! :)"
>>>>>>> 97716f3498f035286d9dafaa544ade3f7028a795
