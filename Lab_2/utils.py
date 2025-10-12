def visualize_pagerank(links_list, ranks_dict):
    import matplotlib.pyplot as plt
    import networkx as nx
    import random

    graph = nx.DiGraph()

    for page, targets in links_list:
        for target in targets:
            graph.add_edge(page, target)

    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(graph, k=2, iterations=50, seed=42)

    ranks = [ranks_dict[node] for node in graph.nodes()]
    min_rank = min(ranks)
    max_rank = max(ranks)
    rank_range = max_rank - min_rank if max_rank > min_rank else 1

    node_sizes = [1000 + (ranks_dict[node] - min_rank) / rank_range * 4000
                  for node in graph.nodes()]

    random.seed(42)
    node_colors = ['#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
                   for _ in graph.nodes()]

    nx.draw_networkx_edges(graph, pos,
                           edge_color='#2E5090',
                           width=2.5,
                           alpha=0.8,
                           arrows=True,
                           arrowsize=25,
                           arrowstyle='-|>',
                           connectionstyle='arc3,rad=0.1',
                           min_source_margin=20,
                           min_target_margin=20)

    nx.draw_networkx_nodes(graph, pos,
                           node_color=node_colors,
                           node_size=node_sizes,
                           alpha=0.9)

    labels = {node: f"{node}\n({ranks_dict[node]:.1f})" for node in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels,
                            font_size=12,
                            font_weight='bold',
                            font_color='white')

    plt.title('PageRank Visualization', fontsize=16, fontweight='bold', pad=20)
    plt.axis('off')
    plt.tight_layout()

    plt.show(block=False)
    plt.pause(0.001)
   