#!flask/bin/python
from flask import Flask, jsonify, request, abort
from Graph import Graph
from JSON import ParseJSON


app = Flask(__name__)


graph = Graph.Graph()
ParseJSON.extract_JSON_info_to_graph(graph)


"""
Allows a user to GET an actor's info by underscore separated name
Returns a list of an object
"""
@app.route('/actors/<value>', methods=['GET'])
def get_actor_no_params(value):
    print("===========================0")
    print(request.args)
    print(value)
    split_actor = value.split("_")
    actor_name = ""
    for part in split_actor:
        actor_name += part + " "
    actor_name = actor_name[0:-1]
    print(actor_name)

    actor_node = graph.find_existing_node(actor_name)

    if actor_node is None:
        return "Input Not Found", 400

    result = []
    result.append({actor_name: {
        "json_class": "Actor",
        "name": actor_name,
        "age": actor_node.age,
        "total_gross": actor_node.revenue,
        "movies": actor_node.films
    }})

    return jsonify(result), 200


"""
Allows a user to GET a list of actors info by a partial name
Returns a list of objects
"""
@app.route('/actors', methods=['GET'])
def get_actor_params():
    print("===========================0")
    print(request.args)

    result = []
    for key in request.args.keys():
        print(key)
        print(request.args[key])

        split_actor = request.args[key].split("_")
        actor_name = ""
        for part in split_actor:
            actor_name += part + " "
        actor_name = actor_name[1:-2]
        print(actor_name)

        if key == "name":
            for node in graph.actors:
                # print(node.name)
                if actor_name in node.name:
                    print("Found something")
                    actor_node = graph.find_existing_node(node.name)
                    result.append({node.name: {
                        "json_class": "Actor",
                        "name": node.name,
                        "age": actor_node.age,
                        "total_gross": actor_node.revenue,
                        "movies": actor_node.films
                    }})

    return jsonify(result), 200

"""
Allows a user to GET a film's info by underscore separated name
Returns a list of an object
"""
@app.route('/movies/<value>', methods=['GET'])
def get_film_no_param(value):
    print("===========================1")
    print(request.args)
    print(value)

    split_film = value.split("_")
    film_name = ""
    for part in split_film:
        film_name += part + " "
    film_name = film_name[0:-1]
    print(film_name)

    film_node = graph.find_existing_node(film_name)

    if film_node is None:
        return "Input Not Found", 400

    result = []
    result.append({film_name: {
        "json_class": "Movie",
        "name": film_node.name,
        "box_office": film_node.revenue,
        "year": film_node.year,
        "actors": film_node.actors
    }})

    return jsonify(result), 200


# @app.route('/movies', methods=['GET'])
# def get_film_params():
#     print("===========================1")
#     print(request.args)
#
#     return jsonify({"G": "H"})


# @app.route('/todo/api/v1.0/tasks', methods=['POST'])
# def create_task():
#     if not request.json or not 'title' in request.json:
#         abort(400)
#     task = {
#         'id': tasks[-1]['id'] + 1,
#         'title': request.json['title'],
#         'description': request.json.get('description', ""),
#         'done': False
#     }
#     tasks.append(task)
#     return jsonify({'task': task}), 201


