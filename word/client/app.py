from ._common import default_api_key, get_template_t1_string, get_api_url, template1, template2, t1_requests, \
    t2_requests
from ..core import Word
import requests
import json

api_protocol = "https://"
api_host = "fourtytwowords.herokuapp.com"


# TODO: write request wrapper like conn
def _make_request(api_url):
    session = requests.session()
    result = session.get(api_url)
    res = json.dumps(result)
    return res

def _execute(operation, word=None, suffix=None):
    api_enpoint = ""
    if operation in t1_requests:
        api_enpoint = get_template_t1_string(template1, word=word, suffix=suffix)
    elif operation in t2_requests:
        api_enpoint = get_template_t1_string(template2)
    api_url = get_api_url(api_protocol, api_host, api_enpoint, default_api_key)
    body = json.loads(_make_request(api_url))
    return body[operation]


def definations(word):
    return _execute("definations", word, "definations")


def examples(word):
    return _execute("examples", word, "definations")


def synonyms(word):
    result = _execute("relatedWords", word, "relatedWords")
    return result["synonyms"]


def antonyms(word):
    result = _execute("relatedWords", word, "relatedWords")
    return result["antonyms"]


def random_word():
    return _execute("randomWord")


def all_results(word=None):
    if word is None:
        word = random_word()

    defn = definations(word)
    ex = examples(word)
    syn = synonyms(word)
    ant = antonyms(word)

    word = Word(literal_value=word, definations=defn, examples=ex, syn=syn, ant=ant)
    return word

