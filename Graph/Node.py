
class Node:

    """
    Constructor for a generic node
    """
    def __init__(self, name, revenue):
        self.name = name
        self.revenue = revenue
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


class Actor(Node):

    films = []

    """
    Constructor for a actor node
    """
    def __init__(self, name, revenue, age, films):
        Node.__init__(self, name, revenue)
        self.age = age
        self.films = films


class Film(Node):

    actors = []

    """
    Constructor for a film node
    """
    def __init__(self, name, revenue, year, actors):
        Node.__init__(self, name, revenue)
        self.year = year
        self.actors = actors
