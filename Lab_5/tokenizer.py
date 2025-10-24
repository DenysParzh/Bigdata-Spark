import re


class Tokenizer:
    def __init__(self):
        self.ids_tokens = {}
        self.tokens_ids = {}
        self.encode_pattern = r'([,.:;?_!"()\']|--|\s)'
        self.decode_pattern = r'\s+([,.?!"()\'])'

    def update_vocabulary(self, text: str):
        tokens = list(set(self._tokenize(text)))
        self.ids_tokens = {code: item for code, item in enumerate(tokens)}
        self.tokens_ids = {item: code for code, item in self.ids_tokens.items()}

        print(self.ids_tokens)

    def encode(self, text: str):
        tokens = self._tokenize(text)
        coded_text = [self.tokens_ids[i] for i in tokens]
        return coded_text

    def decode(self, ids: list[int]):
        untokenize_text = " ".join([self.ids_tokens[id] for id in ids])
        output_text = re.sub(self.decode_pattern, r'\1', untokenize_text)
        return output_text

    def _tokenize(self, text):
        result = re.split(self.encode_pattern, text)
        return [item.strip() for item in result if item.strip()]
