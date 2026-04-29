import collections
from turtle import st


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}

    def add_vertex(self, vertex_label):
        self.vertices.add(vertex_label)

    def add_edge(self, start, end, distance):
        self.edges[start].append(end)
        self.distances[(start, end)] = distance

    def show_grah(self):
        text = 'E D G E S        COSTS'
        print(text, '\n***********************')
        for key in self.distances.keys():
            print(key, ' ---> ', self.distances[key])
        print('***********************')
