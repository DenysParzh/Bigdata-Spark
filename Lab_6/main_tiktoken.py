import tiktoken


def test(tokenizer):
    text = (
        "Lavondyss has won, or been nominated <|endoftext|> "
        "for, rather fantasy literature awards."
    )

    ids = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
    print(ids)

    result_text = tokenizer.decode(ids)
    print(result_text)


def main():
    tokenizer = tiktoken.get_encoding("gpt2")
    test(tokenizer)


if __name__ == "__main__":
    main()
