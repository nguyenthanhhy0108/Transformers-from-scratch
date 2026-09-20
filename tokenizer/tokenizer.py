from pathlib import Path

from tokenizers import Tokenizer


TOKENIZER_PATH = (
    Path(__file__).resolve().parent.parent
    / "resources"
    / "tokenizer"
    / "qwen3.json"
)


class TokenizerWrapper:
    def __init__(self, path: str | Path = TOKENIZER_PATH):
        """Wrapper around the Hugging Face Tokenizers tokenizer.

        Will use default .json file in resoures folder if input path is empty
        """
        self.tokenizer = Tokenizer.from_file(str(path))

    def encode(self, text: str) -> list[int]:
        """
        Input text, return token ids
        """
        return self.tokenizer.encode(text).ids

    def decode(self, ids: list[int]) -> str:
        """
        Input token ids, return text
        """
        return self.tokenizer.decode(ids)

    def tokenize(self, text: str) -> list[str]:
        """
        Input text, return tokens
        """
        return self.tokenizer.encode(text).tokens

    @property
    def vocab_size(self) -> int:
        return self.tokenizer.get_vocab_size()