
class Edge:

    """
    Constructor for a new edge
    """
    def __init__(self, start_node, end_node, weight_value):
        self.edge_nodes = (start_node, end_node)
        self.weight = weight_value
