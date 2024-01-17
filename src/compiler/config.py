
# type-regex pair token dictionary

TOKEN_DICT = {
    "IDENTIFIER": r'(?P<IDENTIFIER>_?[A-Za-z_]+[a-zA-Z0-9_]*)',
    "INT_LITERAL": r'(?P<INT_LITERAL>\-?\b[1-9][0-9]*\b|\b0\b)',
    "NEWLINE": r'(?P<NEWLINE>\n)',
    "WHITESPACE": r'(?P<WHITESPACE>[ \t]+)',
    "EXCEPT": r'(?P<EXCEPT>.)',
}
