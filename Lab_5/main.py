from core.utils import load_vocabulary
from tokenizer import Tokenizer


def test1(tokenizer):
    vocabulary = load_vocabulary("the-verdict.txt")
    tokenizer.update_vocabulary(vocabulary)

    text = """
            "It's the last he painted, you know,"
            Mrs. Gisburn said with pardonable pride.
           """
    print("\nBase test 1: ")
    coded = tokenizer.encode(text)
    print(coded)

    decoded = tokenizer.decode(coded)
    print(decoded)

    text = """
            Hello, do you like tea?
           """
    try:
        print("\nKey error test: ")
        coded = tokenizer.encode(text)
        print(coded)

        decoded = tokenizer.decode(coded)
        print(decoded)
    except KeyError as e:
        print(f"Key error: {e}")


def test2(tokenizer):
    vocabulary = load_vocabulary("lavondyss.txt")
    tokenizer.update_vocabulary(vocabulary)

    text = """
            Mythago Wood and Lavondyss have been described by Michael D. C. Drout
           """
    print("\nBase test 2: ")
    coded = tokenizer.encode(text)
    print(coded)

    decoded = tokenizer.decode(coded)
    print(decoded)

    print("\nTest lowercase: ")
    text = """
             john clute
            """
    try:
        coded = tokenizer.encode(text)
        print(coded)

        decoded = tokenizer.decode(coded)
        print(decoded)

    except KeyError as e:
        print(f"Key error: {e}")

    text_lower = """
                    john clute
                 """
    text_upper = """
                    John Clute
                 """
    print("\nTest lowercase equals: ")
    try:
        coded = tokenizer.encode(text_lower)
        print(coded)

        coded = tokenizer.encode(text_upper)
        print(coded)

    except KeyError as e:
        print(f"Key error: {e}")


def main():
    tokenizer = Tokenizer()

    test1(tokenizer)
    test2(tokenizer)


if __name__ == "__main__":
    main()
