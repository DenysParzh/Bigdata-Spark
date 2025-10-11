import os
from collections import defaultdict

from core.utils import text_preprocessing


def mapper(filename, body):
    basename = os.path.basename(filename)
    clear_body = text_preprocessing(body)
    words = clear_body.split()
    return [(word, (basename, pos)) for pos, word in enumerate(words, 1)]


def format_content(items):
    file_offsets = defaultdict(list)
    for basename, pos in items:
        file_offsets[basename].append(pos)

    formatted_parts = []
    for basename in sorted(file_offsets.keys()):
        offsets = sorted(file_offsets[basename])
        offsets_str = ', '.join(map(str, offsets))
        formatted_parts.append(f"{basename}@{offsets_str}")

    return ' | '.join(formatted_parts)


def view(result):
    print(" - Inverted index - ")

    for word, content in result:
        print(f"{word} - {content}")


def inverted_index(text_resources):
    ii = text_resources.flatMap(lambda x: mapper(x[0], x[1]))

    grouped_ii = ii.groupByKey()
    formatted_ii = grouped_ii.map(lambda x: (x[0], format_content(x[1])))
    sorted_ii = formatted_ii.sortByKey()

    result = sorted_ii.collect()

    view(result)
