import unittest
import requests

from Graph import Graph
from JSON import ParseJSON
import Analysis


class TestMethods(unittest.TestCase):

    """
    Makes sure that nodes are entered into the graph correctly
    """
    def test_add_nodes_to_graph(self):
        graph = Graph.Graph()
        graph.add_actor_to_graph("Bob", 500, 40, [])
        graph.add_actor_to_graph("Salad", 1000, 67, [])
        graph.add_film_to_graph("Best Movie Ever", 50000, 2019, [])
        self.assertEqual(2, graph.actor_count)
        self.assertEqual(1, graph.film_count)

    """
    Checks to make sure that the information for each node is correct
    """
    def test_hayden_christensen(self):
        graph = Graph.Graph()
        ParseJSON.extract_JSON_info_to_graph(graph)
        hayden_node = graph.find_existing_node("Hayden Christensen")
        self.assertEqual("Hayden Christensen", hayden_node.name)
        self.assertEqual(0, hayden_node.revenue)
        self.assertEqual(35, hayden_node.age)
        self.assertEqual(21, len(hayden_node.films))

    """
    Makes sure that searching for an existing node returns the node
    """
    def test_unbreakable_node(self):
        graph = Graph.Graph()
        ParseJSON.extract_JSON_info_to_graph(graph)
        unbreakable_node = graph.find_existing_node("Unbreakable")
        self.assertEqual("Unbreakable", unbreakable_node.name)

    """
    Makes sure that searching for a non-existent node returns None
    """
    def test_disney_the_kid_node(self):
        graph = Graph.Graph()
        ParseJSON.extract_JSON_info_to_graph(graph)
        disney_the_kid_node = graph.find_existing_node("Disney's The Kid")
        self.assertEqual(None, disney_the_kid_node)

    """
    Make sure I can find the age min and max for the actors
    """
    def test_analysis_age_range(self):
        graph = Graph.Graph()
        ParseJSON.extract_JSON_info_to_graph(graph)
        Analysis.oldest_and_youngest_actors(graph)
        Analysis.oldest_and_youngest(graph)

    """
    Make sure the analysis for gross total by age group runs
    """
    def test_age_group_money(self):
        graph = Graph.Graph()
        ParseJSON.extract_JSON_info_to_graph(graph)
        (money_dict, people_count_dict) = Analysis.age_group_money(graph)
        print(people_count_dict)
        self.assertEqual({'20-29': 21767523, '30-39': 2216132, '40-49': 178215118, '50-59': 1027863196, '60-69': 1005774688, '70-79': 1001143377, '80-89': 1150162485, '90-99': 16325523}, money_dict)
        self.assertEqual({'20-29_count': 11, '30-39_count': 41, '40-49_count': 59, '50-59_count': 83, '60-69_count': 56, '70-79_count': 29, '80-89_count': 19, '90-99_count': 4}, people_count_dict)

    """
    Make sure the analysis for age group correlation runs
    """
    def test_age_group_correlation(self):
        graph = Graph.Graph()
        ParseJSON.extract_JSON_info_to_graph(graph)
        (money_dict, people_count_dict) = Analysis.age_group_money(graph)
        Analysis.age_group_correlation(money_dict, people_count_dict)

    """
    Make sure the analysis for hub actors runs
    """
    def test_hub_actors(self):
        graph = Graph.Graph()
        ParseJSON.extract_JSON_info_to_graph(graph)
        Analysis.hub_actors(graph)

    """
    Make sure the analysis for average films per actor runs
    """
    def test_films_per_actor_per_age_group(self):
        graph = Graph.Graph()
        ParseJSON.extract_JSON_info_to_graph(graph)
        Analysis.films_per_actor_per_age_group(graph)

    """
    API test for just an actor name
    """
    def test_API_actor_bruce_willis(self):
        URL = "http://127.0.0.1:5000/actors/Bruce_Willis"
        r = requests.get(url = URL)
        data = r.json()
        self.assertEqual([{"Bruce Willis":{"age":61,"json_class":"Actor","movies":["The First Deadly Sin","The Verdict","Blind Date","Sunset","Die Hard","In Country","Look Who's Talking","That's Adequate","Die Hard 2","Look Who's Talking Too","The Bonfire of the Vanities","Mortal Thoughts","Hudson Hawk","Billy Bathgate","The Last Boy Scout","The Player","Death Becomes Her","Loaded Weapon 1","Striking Distance","Color of Night","North","Pulp Fiction","Nobody's Fool","Die Hard with a Vengeance","Four Rooms","12 Monkeys","Last Man Standing","Beavis and Butt-Head Do America","The Fifth Element","The Jackal","Mercury Rising","Armageddon","The Siege","Breakfast of Champions","The Sixth Sense","The Story of Us","The Whole Nine Yards","Disney's The Kid","Unbreakable","Bandits","Hart's War","True West","The Crocodile Hunter: Collision Course","Grand Champion","Tears of the Sun","Rugrats Go Wild","Charlie's Angels: Full Throttle","The Whole Ten Yards","Ocean's Twelve","Hostage","Sin City","Alpha Dog","16 Blocks","Fast Food Nation","Lucky Number Slevin","Over the Hedge","Hammy's Boomerang Adventure","The Astronaut Farmer","Perfect Stranger","Grindhouse","Planet Terror","Nancy Drew","Live Free or Die Hard","What Just Happened","Assassination of a High School President","Surrogates","Cop Out","The Expendables","Red","Set Up","Catch .44","Moonrise Kingdom","Lay the Favorite","The Expendables 2","The Cold Light of Day","Looper","Fire with Fire","A Good Day to Die Hard","G.I. Joe: Retaliation","Red 2","Sin City: A Dame to Kill For","The Prince","Vice","Rock the Kasbah","Extraction","Precious Cargo","Marauders","Split","The Bombing","Once Upon a Time in Venice","First Kill","Death Wish"],"name":"Bruce Willis","total_gross":562709189}}], data)

    """
    API test for a partial actor name
    """
    def test_API_actor_morgan(self):
        URL = "http://127.0.0.1:5000/actors?name=%E2%80%9DMorgan%E2%80%9D"
        r = requests.get(url = URL)
        data = r.json()
        self.assertEqual([{"Morgan Freeman":{"age":79,"json_class":"Actor","movies":["The Pawnbroker","A Man Called Adam","Where Were You When the Lights Went Out?","Brubaker","Eyewitness","Teachers","Harry & Son","Marie","That Was Then... This Is Now","Street Smart","Clean and Sober","Glory","Driving Miss Daisy","Lean on Me","Johnny Handsome","The Civil War","The Bonfire of the Vanities","Robin Hood: Prince of Thieves","Unforgiven","The Power of One","Bopha!","The Shawshank Redemption","Outbreak","Seven","Chain Reaction","Moll Flanders","Amistad","Kiss the Girls","Deep Impact","Hard Rain","Nurse Betty","Under Suspicion","Along Came a Spider","The Sum of All Fears","High Crimes","Bruce Almighty","Dreamcatcher","Levity","The Big Bounce","Million Dollar Baby","An Unfinished Life","War of the Worlds","Batman Begins","Unleashed","Magnificent Desolation: Walking on the Moon 3D","Edison Force","The Contract","Lucky Number Slevin","10 Items or Less","Evan Almighty","Feast of Love","Gone Baby Gone","The Bucket List","Wanted","The Love Guru","The Dark Knight","Thick as Thieves","The Maiden Heist","Invictus","RED","Conan the Barbarian","Dolphin Tale","The Magic of Belle Isle","The Dark Knight Rises","Olympus Has Fallen","Oblivion","Now You See Me","Last Vegas","The Lego Movie","Transcendence","Lucy","Dolphin Tale 2","5 Flights Up","Lennon or McCartney","Last Knights","Ted 2","Momentum","London Has Fallen","Now You See Me 2","Ben-Hur","Going in Style","Villa Capri"],"name":"Morgan Freeman","total_gross":20556228}},{"Tracy Morgan":{"age":48,"json_class":"Actor","movies":["A Thin Line Between Love and Hate","Half Baked","Bamboozled","How High","Jay and Silent Bob Strike Back","30 Years to Life","Head of State","The Longest Yard","Are We There Yet?","Little Man","VH1's Totally Awesome","Farce of the Penguins","First Sunday","Superhero Movie","G-Force","Deep in the Valley","Cop Out","Death at a Funeral","The Other Guys","Rio","The Son of No One","Why Stop Now","Rio 2","The Boxtrolls","Top Five","Lennon or McCartney","Accidental Love","The Night Before","Fist Fight","The Star","The Clapper"],"name":"Tracy Morgan","total_gross":55}}], data)

    """
    API test for a film name
    """
    def test_API_film_pulp_fiction(self):
        URL = "http://127.0.0.1:5000/movies/Pulp_Fiction"
        r = requests.get(url = URL)
        data = r.json()
        self.assertEqual([{"Pulp Fiction":{"actors":["John Travolta","Samuel L. Jackson","Uma Thurman","Harvey Keitel","Tim Roth","Amanda Plummer","Maria de Medeiros","Ving Rhames","Eric Stoltz","Rosanna Arquette","Christopher Walken","Bruce Willis"],"box_office":213,"json_class":"Movie","name":"Pulp Fiction","year":1994}}], data)


if __name__ == '__main__':
    unittest.main()
