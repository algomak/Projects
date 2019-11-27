import logging
import random

from .common import _let_user_try, _generate_random_syn_or_ant
from client import all_results

log = logging.getLogger(__name__)


def play(word=None):
    """

    :param word:
    :return:
    """
    if word is None:
        word = all_results()
    rand_syn_or_ant = _generate_random_syn_or_ant(word)
    log.info("Guess the word!")
    rand_defn = random.choice(word.definations)
    log.info(f'defination: {rand_defn}\n'
             f'{rand_syn_or_ant}')
    log.info("Enter guessed word: ")
    # making extended map with random attributes inside
    game_word = {
        'word': word,
        'defn': rand_defn
    }
    if 'synonym' in rand_syn_or_ant:
        game_word['synonym'] = rand_syn_or_ant
    else:
        game_word['antonym'] = rand_syn_or_ant
    return _let_user_try(game_word)