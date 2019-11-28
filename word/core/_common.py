import logging
import random
from .word import Word

log = logging.getLogger(__name__)

_choices_list = ['Try Again!', 'Hint', 'Quit']


def _get_user_input(msg="Enter your response: "):
    print(msg)
    return str(input())


def _get_another_randomly(word: Word, attribute: str, curr_value: str = None):
    """

    :param word:
    :param attribute: synonym, antonym, definition, example
    :return:
    """
    log.info(f"getting another value for attribute: {attribute}, word: {word.literal_value}")
    if attribute in word.__dict__:
        if getattr(word, attribute) is not None:
            attribute_list = list(getattr(word, attribute))
            if len(attribute_list) > 1:
                if curr_value in attribute_list:
                    attribute_list.remove(curr_value)
                return random.choice(attribute_list)
        else:
            return None
    else:
        log.info(f"Wrong attribute value, available attributes: {list(word.__dict__.keys())}")


def _print_list(anylist: list, list_title=None) -> None:
    """

    :param anylist:
    :return:
    """
    if list_title is not None:
        print(list_title)
    for idx, element in enumerate(anylist):
        print(f"{idx + 1}: {element}")
    print("\n")


_word_structure = {
    "literal_value": "Word",
    "defn": "Definations",
    "ex": "Examples",
    "syn": "Synonyms",
    "ant": "Antonyms"
}


def print_pretty(object):
    """
    utility function for printing
    :return:
    """
    if isinstance(object, list):
        _print_list(object)
    elif isinstance(object, Word):
        for key, value in object.__dict__.items():
            if isinstance(value, list):
                _print_list(value, _word_structure[key])
            else:
                print(f"{_word_structure[key]}: {value}\n")
