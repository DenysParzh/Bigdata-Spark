import re


def text_preprocessing(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text.lower())


def mapper(line: str) -> list[tuple[str, int]]:
    clear_line = text_preprocessing(line)
    return [(word, 1) for word in clear_line.split()]


def view(data):
    print(" - Count word in files - ")
    for word, count in data:
        print(f"{word} - {count}")


def count_words(text_resources):
    mapped = text_resources.flatMap(mapper)
    reduced = mapped.reduceByKey(lambda a, b: a + b)
    collected = reduced.collect()

    view(collected)
