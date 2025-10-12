import findspark

from core import session
from pagerank import parse_page_relations, pagerank
from utils import visualize_pagerank

findspark.init()


def display_relations(links):
    print(" - Page Relations - ")

    for page, page_links in links.collect():
        print(f"  {page} -> {page_links}")
    print()


def display_result(results):
    for page, rank in results:
        print(f"{page}: {rank:.6f}")


def main():
    spark_session = session.build()
    spark_context = spark_session.sparkContext

    num_iterations = 1
    damping_factor = 0.85
    input_page_graph = "input_page_graph.txt"

    links = parse_page_relations(spark_context, input_page_graph)

    display_relations(links)

    ranks = links.map(lambda page_links: (page_links[0], 1.0))
    ranks = pagerank(links, ranks, damping_factor, num_iterations)
    results = sorted(ranks.collect(), key=lambda x: x[0])

    display_result(results)

    links_list = links.collect()
    ranks_dict = dict(ranks.collect())
    visualize_pagerank(links_list, ranks_dict)

    spark_session.stop()


if __name__ == "__main__":
    main()
