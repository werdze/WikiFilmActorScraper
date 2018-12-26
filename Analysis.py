import matplotlib.pyplot as plt

from Graph import Graph


"""
Finds the youngest and oldest actors in an efficient/shorter way
"""
# Credit to Patrick Hurtado for oldest_and_youngest
def oldest_and_youngest(graph):
    o = sorted(graph.actors, key=lambda actor: actor.age)[-1].age
    youngest = sorted(list(filter(lambda actor: actor.age != -1, graph.actors)), key=lambda actor: actor.age)[0]
    print(youngest.name, youngest.age)

"""
Finds the youngest and oldest actors in a more readable way
"""
def oldest_and_youngest_actors(graph):
    oldest_age = 0
    youngest_age = 100
    oldest_name = ""
    youngest_name = ""
    for actor in graph.actors:
        if actor.age > oldest_age:
            oldest_age = actor.age
            oldest_name = actor.name
        if actor.age < youngest_age and actor.age > 0:
            youngest_age = actor.age
            youngest_name = actor.name
    print("Oldest actor: " + str(oldest_age) + " " + oldest_name + " and youngest actor: " + str(youngest_age) + " " + youngest_name)

"""
Finds how much money each age groups make and creates a graph to represent it
"""
def age_group_money(graph):
    money_dict = {"20-29": 0, "30-39": 0, "40-49": 0, "50-59": 0, "60-69": 0, "70-79": 0, "80-89": 0, "90-99": 0}
    people_count_dict = {"20-29_count": 0, "30-39_count": 0, "40-49_count": 0, "50-59_count": 0, "60-69_count": 0, "70-79_count": 0, "80-89_count": 0, "90-99_count": 0}

    for actor in graph.actors:
        if actor.age >= 20 and actor.age < 30:
            money_dict["20-29"] += actor.revenue
            people_count_dict["20-29_count"] += 1
        elif actor.age >= 30 and actor.age < 40:
            money_dict["30-39"] += actor.revenue
            people_count_dict["30-39_count"] += 1
        elif actor.age >= 40 and actor.age < 50:
            money_dict["40-49"] += actor.revenue
            people_count_dict["40-49_count"] += 1
        elif actor.age >= 50 and actor.age < 60:
            money_dict["50-59"] += actor.revenue
            people_count_dict["50-59_count"] += 1
        elif actor.age >= 60 and actor.age < 70:
            money_dict["60-69"] += actor.revenue
            people_count_dict["60-69_count"] += 1
        elif actor.age >= 70 and actor.age < 80:
            money_dict["70-79"] += actor.revenue
            people_count_dict["70-79_count"] += 1
        elif actor.age >= 80 and actor.age < 90:
            money_dict["80-89"] += actor.revenue
            people_count_dict["80-89_count"] += 1
        elif actor.age >= 90 and actor.age < 100:
            money_dict["90-99"] += actor.revenue
            people_count_dict["90-99_count"] += 1

    max_revenue = 0
    max_range = ""
    for key in money_dict.keys():
        if money_dict[key] > max_revenue:
            max_revenue = money_dict[key]
            max_range = key
    print("Is there an age group that generates the most amount of money?")
    print("Age group: " + max_range, "Gross Total: " + str(max_revenue))

    x_axis_values = []
    y_axis_values = []
    for key in money_dict.keys():
        x_axis_values.append(key)
        y_axis_values.append(money_dict[key])
    plt.bar(x_axis_values, y_axis_values)
    plt.suptitle('Gross Total by Age Group')
    plt.xlabel('Age Groups')
    plt.ylabel('USD')
    plt.show()

    return (money_dict, people_count_dict)

"""
Finds how much money each age groups make compared to the number of people in each age group and creates a graph to represent it
"""
def age_group_correlation(money_dict, people_count_dict):
    correlations = []
    for key in money_dict:
        correlations.append(money_dict[key] / people_count_dict[key + "_count"])
    print("What does the correlation between age and grossing value look like?")
    print(correlations)

    x_axis_values = []
    y_axis_values = correlations
    for key in money_dict.keys():
        x_axis_values.append(key)
    plt.plot(x_axis_values, y_axis_values)
    plt.suptitle('Age Group Correlation')
    plt.xlabel('Age Groups')
    plt.ylabel('Average USD per Actor')
    plt.show()

"""
Finds the actors who have the most number of connections to other actors and creates a graph to represent it
"""
def hub_actors(graph):
    actors_dict = {}
    for actor in graph.actors:
        actors_dict[actor.name] = []
        for film in actor.films:
            film_node = graph.find_existing_node(film)
            if film_node is not None and type(film_node) != Graph.Node.Actor:
                actors_dict[actor.name].extend(film_node.actors)
    actors_arr = []
    for key in actors_dict:
        actors_arr.append((key, len(actors_dict[key])))


    actors_arr.sort(key=lambda x: x[1])
    actors_arr.reverse()
    print(actors_arr)

    x_axis_values = []
    y_axis_values = []
    i = 0
    for (actor_name, fellow_actor_count) in actors_arr:
        x_axis_values.append(actor_name)
        y_axis_values.append(fellow_actor_count)
        i += 1
        if i == 5:
            break
    plt.bar(x_axis_values, y_axis_values)
    plt.suptitle('Hub Actors')
    plt.xlabel('Actors')
    plt.ylabel('# of Actors Worked With')
    plt.show()

"""
Finds the average number of films per actor in each age group
"""
def films_per_actor_per_age_group(graph):
    film_count_dict = {"20-29": 0, "30-39": 0, "40-49": 0, "50-59": 0, "60-69": 0, "70-79": 0, "80-89": 0, "90-99": 0}
    people_count_dict = {"20-29_count": 0, "30-39_count": 0, "40-49_count": 0, "50-59_count": 0, "60-69_count": 0, "70-79_count": 0, "80-89_count": 0, "90-99_count": 0}
    for actor in graph.actors:
        if actor.age >= 20 and actor.age < 30:
            film_count_dict["20-29"] += len(actor.films)
            people_count_dict["20-29_count"] += 1
        elif actor.age >= 30 and actor.age < 40:
            film_count_dict["30-39"] += len(actor.films)
            people_count_dict["30-39_count"] += 1
        elif actor.age >= 40 and actor.age < 50:
            film_count_dict["40-49"] += len(actor.films)
            people_count_dict["40-49_count"] += 1
        elif actor.age >= 50 and actor.age < 60:
            film_count_dict["50-59"] += len(actor.films)
            people_count_dict["50-59_count"] += 1
        elif actor.age >= 60 and actor.age < 70:
            film_count_dict["60-69"] += len(actor.films)
            people_count_dict["60-69_count"] += 1
        elif actor.age >= 70 and actor.age < 80:
            film_count_dict["70-79"] += len(actor.films)
            people_count_dict["70-79_count"] += 1
        elif actor.age >= 80 and actor.age < 90:
            film_count_dict["80-89"] += len(actor.films)
            people_count_dict["80-89_count"] += 1
        elif actor.age >= 90 and actor.age < 100:
            film_count_dict["90-99"] += len(actor.films)
            people_count_dict["90-99_count"] += 1

    x_axis_values = []
    film_per_person = []
    for key in film_count_dict:
        film_per_person.append(film_count_dict[key] / people_count_dict[key + "_count"])
        x_axis_values.append(key)

    plt.bar(x_axis_values, film_per_person)
    plt.suptitle('Average Films per Actor in each Age Group')
    plt.xlabel('Age Groups')
    plt.ylabel('Average Number of Films per Actor')
    plt.show()
