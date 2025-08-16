from collections import defaultdict


def find_shortest_path(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.vertices)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path


def show_min_distances(min_distances, frm):
    text = 'FROM    TO      COST'
    print(text, '\n***********************')
    for key in min_distances.keys():
        print(frm, ' ---> ', key, '  :  ', min_distances.get(key))
    print('***********************')


def show_shortestpath_tree(path, frm):
    path_txt = frm
    for key in path.keys():
        path_txt += " ---> " + key
        text = 'FROM    TO      COST'
    text = "SHORTEST PATH TREE"
    print(text, '\n***********************')
    print(path_txt)
