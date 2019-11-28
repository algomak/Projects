from typing import List
from attr import dataclass


@dataclass
class Word:
    literal_value: str
    defn: List[str]
    ex: List[str]
    syn: List[str]
    ant: List[str]

    def __str__(self) -> str:
        full_dict_str = f"Word: {self.literal_value}\n" \
            f"definitions: {self.defn}\n" \
            f"examples: {self.ex}\n" \
            f"synonyms: {self.syn}\n" \
            f"antonyms: {self.ant}\n"
        return full_dict_str
