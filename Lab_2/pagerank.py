
def relation_parser(raw_relation):
    relation = raw_relation.replace(' ', '')

    [page, links] = relation.split(':')
    links = links.split(',')

    return page, links


def parse_page_relations(driver, path):
    links = (
        driver.textFile(path)
        .map(relation_parser)
        .filter(lambda x: x is not None)
        .cache()
    )

    return links


def pagerank(relation, ranks, damping_factor=0.85, iterations=10):
    for iteration in range(iterations):
        contribs = relation.join(ranks).flatMap(
            lambda page_data: [
                (dest, page_data[1][1] / len(page_data[1][0]))
                for dest in page_data[1][0]
            ]
        )
        ranks = contribs.reduceByKey(lambda x, y: x + y).mapValues(
            lambda rank: (1 - damping_factor) + damping_factor * rank
        )

    return ranks
