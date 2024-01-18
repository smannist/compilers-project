import unittest
from compiler.tokenizer import tokenize
from compiler.custom_token import Token, L

class TestTokenizeFunction(unittest.TestCase):
    def test_source_code_is_tokenized_correctly(self) -> None:
        source_code = "If x is not 10 then return 1"

        expected_tokens = [
            Token(L(0, 0), "IDENTIFIER", "If"),
            Token(L(0, 3), "IDENTIFIER", "x"),
            Token(L(0, 5), "IDENTIFIER", "is"),
            Token(L(0, 8), "IDENTIFIER", "not"),
            Token(L(0, 12), "INT_LITERAL", "10"),
            Token(L(0, 15), "IDENTIFIER", "then"),
            Token(L(0, 20), "IDENTIFIER", "return"),
            Token(L(0, 27), "INT_LITERAL", "1"),
        ]

        actual_tokens = tokenize(source_code)

        for expected, actual in zip(expected_tokens, actual_tokens):
            self.assertEqual(expected.loc, actual.loc)
            self.assertEqual(expected.type, actual.type)
            self.assertEqual(expected.text, actual.text)

    def test_invalid_input_is_not_accepted(self) -> None:
        source_code = "!"

        with self.assertRaises(RuntimeError) as context:
            tokenize(source_code)

        self.assertEqual(str(context.exception),
                         "Caught unexpected value: '!' at position (0,0).")
