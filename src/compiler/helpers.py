import re as regex
from config import TOKEN_DICT

def merge_regex(dict: dict = TOKEN_DICT) -> regex.Pattern:
    return regex.compile("|".join(dict.values()))
