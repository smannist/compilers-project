import re as regex

def tokenize(source_code: str) -> list[str]:
    tokens = []

    identifiers = regex.compile(r'(?P<IDENTIFIER>_?[A-Za-z_]+[a-zA-Z0-9_]*)')
    int_literals = regex.compile(r'(?P<INT_LITERAL>\-?\b[1-9]+\b|\b0\b)')
    newline = regex.compile(r'(?P<NEWLINE>\n)')
    skip = regex.compile(r'(?P<SKIP>[ \t]+)')
    exception = regex.compile(r'(?P<EXCEPT>.|//)')

    merged_regex = regex.compile("|".join(
        [identifiers.pattern, int_literals.pattern, newline.pattern, skip.pattern, exception.pattern]))

    matches = merged_regex.finditer(source_code)

    for match in matches:
        token_type = match.lastgroup
        value = match.group()

        if token_type == "NEWLINE":
            continue
        elif token_type == "SKIP":
            continue
        elif token_type == "EXCEPT":
            raise RuntimeError(f"Invalid character: '{value}'")

        tokens.append(value)

    return tokens
