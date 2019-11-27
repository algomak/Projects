from string import Template
operations = (
    "defn",
    "syn",
    "ant",
    "ex",
    "play",
    "",
)

default_api_key = "b972c7ca44dda72a5b482052b1f5e13470e01477f3fb97c85d5313b3c112627073481104fec2fb1a0cc9d84c2212474c0cbe7d8e59d7b95c7cb32a1133f778abd1857bf934ba06647fda4f59e878d164"

template1 = Template(f"word/$word/$suffix")
template2 = Template(f"/words/randomWord")

#TODO: combine requests with templates
t1_requests = ["examples", "definations", "relatedWords"]
t2_requests = ["randomWord"]

def get_template_t1_string(template: Template, **kwargs):
    temp = template
    word = kwargs.pop("word", None)
    suffix = kwargs.pop("suffix", None)
    if word is not None:
        temp = Template(template.safe_substitute(word=word))
    if suffix is not None:
        temp = Template(template.safe_substitute(suffix=suffix))
    return temp.safe_substitute()


def get_api_url(api_protocol, api_host, api_endpoint, api_key):
    return f"{api_protocol}{api_host}{api_endpoint}?{api_key}"
