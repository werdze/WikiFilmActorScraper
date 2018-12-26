from JSON import ParseJSON
from Graph import Graph
import Utils
import Analysis

"""
Runs the scraper and graph creator, prints the resulting graph, and runs the convert to json function
"""
def main():
    print("===========================")

    graph = Graph.Graph()

    ParseJSON.extract_JSON_info_to_graph(graph)

    # graph.add_remaining_nodes()

    graph.add_all_edges()

    print("\n")
    Utils.Utils.print_graph_nodes_and_edges(graph)
    print()
    Analysis.oldest_and_youngest_actors(graph)
    print()
    (money_dict, people_count_dict) = Analysis.age_group_money(graph)
    print()
    Analysis.age_group_correlation(money_dict, people_count_dict)
    print()
    Analysis.hub_actors(graph)
    print()
    Analysis.films_per_actor_per_age_group(graph)

    return()


if __name__ == "__main__":
    main()