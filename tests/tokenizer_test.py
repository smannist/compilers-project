import unittest
from parameterized import parameterized
from compiler.tokenizer import tokenize
from compiler.custom_token import Token, L

class TestTokenizeFunction(unittest.TestCase):
    def test_source_code_is_tokenized_correctly(self) -> None:
        source_code = "If x is not 10 then return 1 = 5"

        expected_tokens = [
            Token(L(0, 0), "IDENTIFIER", "If"),
            Token(L(0, 3), "IDENTIFIER", "x"),
            Token(L(0, 5), "IDENTIFIER", "is"),
            Token(L(0, 8), "IDENTIFIER", "not"),
            Token(L(0, 12), "INT_LITERAL", "10"),
            Token(L(0, 15), "IDENTIFIER", "then"),
            Token(L(0, 20), "IDENTIFIER", "return"),
            Token(L(0, 27), "INT_LITERAL", "1"),
            Token(L(0, 29), "OPERATOR", "="),
            Token(L(0, 31), "INT_LITERAL", "5"),
        ]

        actual_tokens = tokenize(source_code)

        for expected, actual in zip(expected_tokens, actual_tokens):
            self.assertEqual(expected.loc, actual.loc)
            self.assertEqual(expected.type, actual.type)
            self.assertEqual(expected.text, actual.text)

    @parameterized.expand([
        ("!=", ["OPERATOR", "!="]),
        ("==", ["OPERATOR", "=="]),
        ("<=", ["OPERATOR", "<="]),
        (">=", ["OPERATOR", ">="]),
        ("<", ["OPERATOR", "<"]),
        (">", ["OPERATOR", ">"]),
        ("+", ["OPERATOR", "+"]),
        ("-", ["OPERATOR", "-"]),
        ("*", ["OPERATOR", "*"]),
        ("/", ["OPERATOR", "/"]),
        ("=", ["OPERATOR", "="]),
        ("!=", ["OPERATOR", "!="]),
    ])
    def test_correct_operators_are_recognised(self, source_code, expected):
        expected_token = Token(L(0, 0), expected[0], expected[1])
        actual_tokens = tokenize(source_code)

        self.assertEqual(actual_tokens[0].loc, expected_token.loc)
        self.assertEqual(actual_tokens[0].type, expected_token.type)
        self.assertEqual(actual_tokens[0].text, expected_token.text)

    @parameterized.expand([
        ("!===", ["OPERATOR", "!="]),
        ("===", ["OPERATOR", "=="]),
        ("<=<", ["OPERATOR", "<="]),
        ("<<", ["OPERATOR", "<"]),
        ("!==", ["OPERATOR", "!="]),
        ("*=", ["OPERATOR", "*"]),
        ("//", ["OPERATOR", "/"]),
    ])
    def test_incorrect_operators_raise_a_runtime_error(self, source_code, expected):
        with self.assertRaises(RuntimeError) as context:
            tokenize(source_code)

        self.assertIn("Caught unexpected value", str(context.exception))
