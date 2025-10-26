from core.utils import load_vocabulary
from tokenizer_v2 import TokenizerV2


def test(tokenizer):
    vocabulary = load_vocabulary("../Lab_5/lavondyss.txt")
    tokenizer.update_vocabulary(vocabulary)

    text1 = "Lavondyss has won, or been nominated"
    text2 = "for, rather fantasy literature awards."
    text = f" {TokenizerV2.EOT_TOKEN} ".join((text1, text2))
    print(text)

    coded = tokenizer.encode(text)
    print(coded)

    decoded = tokenizer.decode(coded)
    print(decoded)


def main():
    tokenizer = TokenizerV2()
    test(tokenizer)


if __name__ == "__main__":
    main()
