import re


def text_preprocessing(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text.lower())