# topological sort

def sort(start, edges):
    # init
    for i in edges.keys():
        if start in edges[i]:
            return []
    sort = []

    while edges:
        for i in edges.keys():
            valid = True
            for j in edges.keys():
                if i in edges[j]:
                    valid = False
                    break
            if valid:
                sort.append(i)
                del edges[i]
    return sort

if __name__ == '__main__':
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
    print(sort('A', edges))
