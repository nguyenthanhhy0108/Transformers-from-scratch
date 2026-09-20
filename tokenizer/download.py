from pathlib import Path

from tokenizers import Tokenizer


MODEL = "Qwen/Qwen3-8B-Base"
OUTPUT_PATH = Path("resources/tokenizer/qwen3.json")


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print(f"Downloading tokenizer: {MODEL}")

    tokenizer = Tokenizer.from_pretrained(MODEL)

    tokenizer.save(str(OUTPUT_PATH))

    print(f"Tokenizer saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()