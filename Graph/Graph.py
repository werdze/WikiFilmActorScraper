from Graph import Edge, Node
# import Graph.Edge
# import Graph.Node


class Graph:

    actor_count = 0
    film_count = 0
    edge_count = 0
    actors = []
    films = []
    edges = []

    """
    Finds and returns a certain node
    """
    def find_existing_node(self, name):
        node_ref = None
        for node in self.actors:
            if node.name == name:
                node_ref = node
        if node_ref is None:
            for node in self.films:
                if node.name == name:
                    node_ref = node
        return node_ref

    """
    Finds and returns a certain edge
    """
    def find_existing_edge(self, actor_name, film_name):
        for edge in self.edges:
            (start_node, end_node) = edge.edge_nodes
            if start_node.name == actor_name and end_node.name == film_name:
                return edge
            elif start_node.name == film_name and end_node.name == actor_name:
                return edge
        return None

    """
    Creates a new actor node for the graph
    Adds it to the actor arr and increments the actor_count
    """
    def add_actor_to_graph(self, name, revenue, age, films):
        if self.find_existing_node(name) is None:
            actor_node = Node.Actor(name, revenue, age, films)
            self.actors.append(actor_node)
            self.actor_count += 1
        return

    """
    Creates a new film node for the graph
    Adds it to the film arr and increments the film_count
    """
    def add_film_to_graph(self, name, revenue, year, actors):
        if self.find_existing_node(name) is None:
            actor_node = Node.Film(name, revenue, year, actors)
            self.films.append(actor_node)
            self.film_count += 1
        return

    """
    Calculates how the percentage of the film revenue that each actor listed in the cast of a film should receive
    """
    @staticmethod
    def revenue_percentages(num_to_split_revenue_by):
        revenue_percentages_arr = []
        summation_of_1_to_num = 0

        for currNum in range(num_to_split_revenue_by + 1):
            summation_of_1_to_num += currNum
        for currNum in range(1, num_to_split_revenue_by + 1):
            revenue_percentages_arr.append((100/summation_of_1_to_num * currNum) / 100)

        return revenue_percentages_arr[::-1]

    """
    Finds and returns the amount an actor made for each movie they were in, for use with edge weights
    """
    def find_edge_revenue_amount(self, actor_node, film_node):
        num_to_split_by = len(film_node.actors)
        percentages = Graph.revenue_percentages(num_to_split_by)
        if actor_node.name in film_node.actors:
            actor_index_in_list = film_node.actors.index(actor_node.name)
            return int(percentages[actor_index_in_list] * film_node.revenue)
        return 0

    """
    Adds all of the films and actors to the graph that were only referenced through the actor list or film list in the film and actor nodes, respectively
    """
    def add_remaining_nodes(self):
        for actor_node in self.actors:
            film_list = actor_node.films
            for film_name in film_list:
                if self.find_existing_node(film_name) is None:
                    self.add_film_to_graph(film_name, 0, 0, [])
        for film_node in self.films:
            actor_list = film_node.actors
            for actor_name in actor_list:
                if self.find_existing_node(actor_name) is None:
                    self.add_actor_to_graph(actor_name, 0, 0, [])
        return

    """
    Looks through every actor and film node and adds all edges to the graph
    Skips over potential edges where there is not an existing node for the film or actor
    """
    def add_all_edges(self):
        for actor_node in self.actors:
            film_list = actor_node.films
            for film_name in film_list:
                if self.find_existing_edge(actor_node.name, film_name) is None:
                    film_node = self.find_existing_node(film_name)
                    if film_node is None:
                        continue
                    edge = Edge.Edge(actor_node, film_node, actor_node.revenue)
                    self.edges.append(edge)
                    self.edge_count += 1
        for film_node in self.films:
            actor_list = film_node.actors
            for actor_name in actor_list:
                if self.find_existing_edge(actor_name, film_node.name) is None:
                    actor_node = self.find_existing_node(actor_name)
                    if actor_node is None:
                        continue
                    edge_revenue = self.find_edge_revenue_amount(actor_node, film_node)
                    edge = Edge.Edge(actor_node, film_node, edge_revenue)
                    self.edges.append(edge)
                    self.edge_count += 1
        return
