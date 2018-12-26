import locale

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

class Utils:

    """
    Converts a revenue string found on a wiki site to an int
    """
    @staticmethod
    def convert_revenue_string_to_int(revenue_string):
        result = -1

        if '$' in revenue_string:
            split_on_dollarsign = revenue_string.split("$")
            split_on_dollarsign[1] = split_on_dollarsign[1].replace("\xa0", " ")
            split_on_space = split_on_dollarsign[1].split(" ")
            # first item should just be a number or a comma separated number
            # second item should be 'million' or 'thousand' or 'billion'
            multiply_by_factor = 1
            if len(split_on_space) == 2:
                if split_on_space[1].lower() == "thousand":
                    multiply_by_factor = 1000
                elif split_on_space[1].lower() == "million":
                    multiply_by_factor = 1000000
                elif split_on_space[1].lower() == "billion":
                    multiply_by_factor = 1000000000
            result = locale.atof(split_on_space[0])
            result *= multiply_by_factor
            result = int(result)

        return result

    """
    Prints out all of the nodes and then all of the edges of the graph
    """
    @staticmethod
    def print_graph_nodes_and_edges(graph):
        for node in graph.actors:
            print(node.name + " " + str(node.revenue) + " " + str(node.age) + " " + str(len(node.films)))
            # print(node.films)
        print("==============================================================================")
        for node in graph.films:
            print(node.name + " " + str(node.revenue) + " " + str(node.year) + " " + str(len(node.actors)))
            # print(node.films)
        print("==============================================================================")
        for edge in graph.edges:
            print(edge.edge_nodes[0].name + " " + edge.edge_nodes[1].name + " " + str(edge.weight))

        print("\nGraph has: " + str(graph.film_count) + " films, " + str(graph.actor_count) + " actors, and " + str(graph.edge_count) + " edges")
