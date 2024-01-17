import unittest
from compiler.tokenizer import tokenize

class TestTokenizeFunction(unittest.TestCase):
    def test_source_code_tokenized_correctly(self) -> None:
        source_code = "_tokens_are_cool while for if else 12314 -213213 e1e _e123_ _e_e_e"

        expected_tokens = ["_tokens_are_cool", "while", "for", "if",
                           "else", "12314", "-213213", "e1e", "_e123_", "_e_e_e"]

        tokens = tokenize(source_code)

        self.assertListEqual(tokens, expected_tokens)

    def test_unallowed_characters_will_raise_except(self) -> None:
        source_code = "!!!!"

        with self.assertRaises(RuntimeError) as context:
            tokenize(source_code)

        self.assertEqual(str(context.exception), "Invalid character: '!'")

    def test_empty_string_returns_no_tokens(self) -> None:
        self.assertEqual(tokenize(""), [])
