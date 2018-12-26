import json

"""
Uses data.json to extract the film and actor info and add it into my graph  
"""
def extract_JSON_info_to_graph(graph):
    with open('JSON/data.json') as file:
        data = json.load(file)

    actors = data[0]
    films = data[1]

    actor_keys = actors.keys()
    for key in actor_keys:
        actor_info = actors[key]
        graph.add_actor_to_graph(actor_info["name"], actor_info["total_gross"], actor_info["age"], actor_info["movies"])
    film_keys = films.keys()
    for key in film_keys:
        film_info = films[key]
        graph.add_film_to_graph(film_info["name"], film_info["box_office"], film_info["year"], film_info["actors"])
