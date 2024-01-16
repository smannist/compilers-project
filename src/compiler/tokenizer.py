import re

def tokenize(source_code: str) -> list[str]:
    tokens = []

    keywords = re.compile(r'\b(while|for|if|else|elif)\b')
    variables = re.compile(
        r'\b_[a-zA-Z][A-Za-z0-9_]*\b|\b[a-zA-Z][A-Za-z0-9_]*\b')
    int_literals = re.compile(r'\-?\b[1-9]+\b|\b0\b')

    matches = re.finditer(
        f'{keywords.pattern}|{variables.pattern}|{int_literals.pattern}', source_code)

    for match in matches:
        token = match.group(0)
        tokens.append(token)

    return tokens
