import re


def text_preprocessing(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text.lower())


def load_vocabulary(path):
    with open(path, 'r', encoding='utf-8') as file:
        vocabulary = file.read()

    return vocabulary