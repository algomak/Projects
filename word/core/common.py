import logging
import random

log = logging.getLogger(__name__)


def _generate_random_syn_or_ant(word):
    return random.choice([{"synonym": random.choice(word.syn)},
                          {"antonym": random.choice(word.ant)}])


_choices_list = ['Try Again!', 'Hint', 'Quit']


def _wrong_word_interface(game_word):
    log.info("Wrong Word! select one of below choices")
    while True:
        choices_string = '\n'.join([f'{i+1}: {e}' for i, e in enumerate(_choices_list)])
        print(choices_string)
        user_input = str(input())
        if user_input in _wrong_interface_map:
            _wrong_interface_map[user_input](game_word)
            break
        else:
            log.info("Wrong choice try again!")


def _quit(game_word):
    print(f"Correct answer is: ")
    print(f"{game_word}")
    exit(0)


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

    log.info("Hint: ")
    _hint_interface_map[_get_user_input()](game_word)


def _get_user_input():
    return str(input())


def _let_user_try(game_word):
    word = game_word['word']
    log.info("Enter your word: ")
    user_word = str(input())
    if user_word == word.literal_value or user_word in word.syn:
        return 'Correct answer'
    else:
        _wrong_word_interface(game_word)


def _jumble_word(game_word) -> str:
    word = game_word['word']
    word_list = list(word.literal_value)
    random.shuffle(word_list)
    log.info(f"jumbled word is: {''.join(word_list)}")


def _another_defn(game_word) -> str:
    word = game_word['word']
    curr_defn = game_word['defn']
    new_defn = random.choice(word.definations.remove(curr_defn))
    word.add(curr_defn)
    game_word['defn'] = new_defn
    log.info(f"another defination of word is: {new_defn}")
    return new_defn


def _another_syn(game_word) -> str:
    word = game_word['word']
    curr_syn = game_word['syn']
    new_syn = random.choice(word.syn.remove(curr_syn))
    word.add(curr_syn)
    log.info(f"another synonym of word is: {new_syn}")
    return new_syn


def _another_ant(game_word) -> str:
    word = game_word['word']
    curr_ant = game_word['ant']
    new_ant = random.choice(word.ant.remove(curr_ant))
    word.add(curr_ant)
    log.info(f"another antonym of word is: {new_ant}")
    return new_ant


_wrong_interface_map = {
    '1': _let_user_try,
    '2': _hint,
    '3': _quit
}

_hint_interface_map = {
    '1': _jumble_word,
    '2': _another_defn,
    '3': _another_syn,
    '4': _another_ant
}
