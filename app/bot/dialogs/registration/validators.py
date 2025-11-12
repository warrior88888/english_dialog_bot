import re
from enum import StrEnum, IntEnum
from typing import Type, Union

def type_factory_english_name(text: str) -> str:
    name = text.strip()
    pattern = r"^([A-Z][a-z]*(['-][A-Z][a-z]*)*)( [A-Z][a-z]*(['-][A-Z][a-z]*)*)*$"
    if not (2 <= len(name) <= 50) or not re.match(pattern, name):
        raise ValueError
    return name

def enum_to_list(en: Union[Type[StrEnum], Type[IntEnum]]) -> list:
    return [(e.name, str(e.value)) for e in en]
