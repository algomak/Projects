from typing import List
from attr import dataclass

@dataclass
class Word:
    literal_value: str
    definations: List[str]
    examples: List[str]
    syn: List[str]
    ant: List[str]

    def __str__(self) -> str:
        full_dict_str = f"Word: {self.literal_value}" \
            f"definations: {self.definations}" \
            f"examples: {self.examples}" \
            f"synonyms: {self.syn}" \
            f"antonyms: {self.ant}"
        return full_dict_str


