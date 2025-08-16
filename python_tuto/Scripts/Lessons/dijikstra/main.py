import graph
import dijkstra


if __name__ == '__main__':

    g = graph.Graph()
    start_node = 's'

    g.add_vertex(start_node)
    g.add_vertex('u')
    g.add_vertex('v')
    g.add_vertex('x')
    g.add_vertex('y')

    g.add_edge('s', 'u', 2)
    g.add_edge('s', 'x', 7)
    g.add_edge('u', 'v', 4)
    g.add_edge('u', 'x', 2)
    g.add_edge('x', 'u', 5)
    g.add_edge('x', 'v', 6)
    g.add_edge('v', 'y', 4)
    g.add_edge('y', 'v', 1)
    g.add_edge('x', 'y', 3)
    g.add_edge('y', 's', 8)

    visited, path = dijkstra.find_shortest_path(g, start_node)
    g.show_grah()
    dijkstra.show_min_distances(visited, start_node)
    dijkstra.show_shortestpath_tree(path, start_node)
