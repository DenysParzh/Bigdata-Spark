import re


class TokenizerV2:
    EOT_TOKEN: str = "<|endoftext|>"
    UNK_TOKEN: str = "<|unk|>"

    def __init__(self):
        self.ids_tokens = {}
        self.tokens_ids = {}
        self.encode_pattern = r'([,.:;?_!"()\']|--|\s)'
        self.decode_pattern = r'\s+([,.?!"()\'])'

    def update_vocabulary(self, text: str):
        tokens = list(set(self._tokenize(text)))
        tokens.extend([self.EOT_TOKEN, self.UNK_TOKEN])

        self.ids_tokens = {code: item for code, item in enumerate(tokens)}
        self.tokens_ids = {item: code for code, item in self.ids_tokens.items()}

    def encode(self, text: str):
        tokens = self._encode_tokenize(text)
        coded_text = [self.tokens_ids[i] for i in tokens]
        return coded_text

    def decode(self, ids: list[int]):
        untokenize_text = " ".join([self.ids_tokens[id] for id in ids])
        output_text = re.sub(self.decode_pattern, r'\1', untokenize_text)
        return output_text

    def _tokenize(self, text):
        result = re.split(self.encode_pattern, text)
        return [item.strip() for item in result if item.strip()]

    def _encode_tokenize(self, text):
        result = self._tokenize(text)
        result = [item if (item in self.tokens_ids) else self.UNK_TOKEN for item in result]
        return result
