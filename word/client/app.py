from ._common import default_api_key, get_template_string, get_api_url, template1, template2, t1_requests, \
    t2_requests
from core import word
import requests
import json
from typing import List
import logging

log = logging.getLogger(__name__)

api_protocol = "https://"
api_host = "fourtytwowords.herokuapp.com"


# TODO: write request wrapper like conn
def _make_request(api_url):
    session = requests.session()
    result = session.get(api_url)
    result.raise_for_status()
    res = result.text
    return res


def _execute(operation, word_str=None, suffix=None):
    log.debug(f"performing operation: {operation}, word: {word_str}")
    api_enpoint = ""
    if operation in t1_requests:
        api_enpoint = get_template_string(template1, word=word_str, suffix=suffix)
    elif operation in t2_requests:
        api_enpoint = get_template_string(template2)
    api_url = get_api_url(api_protocol, api_host, api_enpoint, default_api_key)
    body = json.loads(_make_request(api_url))
    return body


def _extraxct_text(anylist: List):
    """
    helper function for schema of examples and definitions apis
    :param anylist:
    :return:
    takes list of objects:
    object: "{text: str }"
    """
    return [e['text'] for e in anylist]


def definitions(word_str) -> List[str]:
    results = _execute("definitions", word_str, "definitions")
    return _extraxct_text(results)


def examples(word_str) -> List[str]:
    results = _execute("examples", word_str, "examples")
    return _extraxct_text(results["examples"])


# immutable tuple to maintain order
_filter_tuple = ('synonym', 'antonym')


# diverse function
def _related_words(word_str):
    """

    :param word:
    :param _filter:
    :return:
    """
    results = _execute("relatedWords", word_str, "relatedWords")
    return results


def _filter_related_words(related_word_resp, filter=None):
    """
    helper function to filter related words from api response
    :param related_word_dict:
    :return:
    """
    if filter not in _filter_tuple:
        return None
    for element in related_word_resp:
        if element['relationshipType'] == filter:
            return element['words']


def synonyms(word_str: str) -> List[str]:
    results = _related_words(word_str)
    for element in results:
        if element['relationshipType'] == 'synonym':
            return element['words']


def antonyms(word_str: str) -> List[str]:
    results = _related_words(word_str)
    for element in results:
        if element['relationshipType'] == 'antonym':
            return element['words']


def random_word() -> str:
    result = _execute("randomWord")
    return result['word']


def all_results(word_str=None):
    if word_str is None:
        word_str = random_word()

    defn = definitions(word_str)
    ex = examples(word_str)
    # single third party call for both syn and antonyms
    related_words = _related_words(word_str)
    syn = _filter_related_words(related_words, 'synonym')
    ant = _filter_related_words(related_words, 'antonym')
    word_obj = word.Word(literal_value=word_str, defn=defn, ex=ex, syn=syn, ant=ant)
    return word_obj
