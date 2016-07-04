class PersonNode(object):
    """ Node in a graph representing a person """

    def __init__(self, name, adjacent=None):
        """ Create a person node with friends adjacent """

        adjacent = adjacent or set()
        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        """ Debugging-friendly representation """

        return "PersonNode: %s" % self.name


class FriendGraph(object):
    """ Create a graph of friends and adjacent friends """

    def __init__(self):
        """ Create an empty graph """

        self.nodes = set()

    def __repr__(self):

        return "FriendGraph: %s" % [n.node for n in self.nodes]

    def add_person(self, person):
        """ Add a person to the graph """

        self.nodes.add(person)

    def add_adjacent(self, person1, person2):
        """ Set two people as friends """

        person2.adjacent.add(person1)
        person1.adjacent.add(person2)
