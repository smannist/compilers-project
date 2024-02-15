import re as regex
from helpers import merge_regex
from custom_token import Token, L

def tokenize(source_code: str) -> list[Token]:
    tokens = []

    line = 0
    column = 0

    for match in regex.finditer(merge_regex(), source_code):
        token_type = match.lastgroup
        value = match.group()

        if token_type == "NEWLINE":
            line += 1
            column = 0
            continue
        elif token_type == "WHITESPACE":
            column += len(value)
            continue
        elif token_type == "COMMENT":
            column += len(value)
            line += 1
            continue
        elif token_type == "EXCEPT":
            raise RuntimeError(
                f"Caught unexpected value: '{value}' at position ({line},{column}).")

        tokens.append(Token(L(line, column), token_type, value))

        column += len(value)

    return tokens
