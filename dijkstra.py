# dijkstra
# heavily borrowed from https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python

def dijkstra(start, edges, nodes):

    currentDist = 0
    current = start
    visited = {}
    unvisited = {node: None for node in nodes}
    unvisited[current] = currentDist

    while True:
        for neighbor, dist in edges[current].items():
            if neighbor in unvisited:
                newDist = currentDist + dist
                if unvisited[neighbor] is None or unvisited[neighbor] > newDist:
                    unvisited[neighbor] = newDist
        visited[current] = currentDist
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDist = sorted(candidates, key = lambda x: x[1])[0]

    return visited


if __name__ == '__main__':
    nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K')
    edges = {
        'A': {'B': 3, 'C': 4, 'D': 2},
        'B': {'G': 2},
        'C': {'F': 3, 'E': 5},
        'D': {'E': 3},
        'E': {'F': 1, 'J': 7},
        'F': {'H': 1, 'J': 1},
        'G': {'H': 3, 'I': 7},
        'H': {'I': 2, 'K': 6},
        'I': {'K': 5},
        'J': {'K': 8},
        'K': {}
    }
    print(dijkstra('A', edges, nodes))
