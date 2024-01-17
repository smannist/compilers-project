import re as regex
from compiler.helpers import merge_regex
from compiler.custom_token import Token, L

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
        elif token_type == "EXCEPT":
            raise RuntimeError(
                f"Caught unexpected value: '{value}' at position ({line}, {column}).")

        tokens.append(Token(L(line, column), token_type, value))

        column += len(value)

    return tokens


if __name__ == "__main__":
    tokens = (
        tokenize("if it works do not touch it \nby great philosopher of 2024"))

    for token in tokens:
        print(token)
