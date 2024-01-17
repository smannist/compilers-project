import re as regex
from config import TOKEN_DICT

def merge_regex(dict=TOKEN_DICT):
    return regex.compile("|".join(dict.values()))
