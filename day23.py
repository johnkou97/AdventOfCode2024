from itertools import combinations

def ParseInput(connections: list) -> dict:
    '''
    Parse the input data and create a graph representation of the connections
    '''
    graph = {}
    for a, b in connections:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph

def FindTriangles(graph: dict) -> set:
    '''
    Find all triangles in the graph
    A triangle is a set of 3 nodes that are all connected to each other
    Uses the itertools combinations function to find all possible triangles
    '''
    triangles = set()
    for node1 in graph:
        for node2, node3 in combinations(graph[node1], 2):
            if node2 in graph[node3]:  # Check if node2 and node3 are connected
                triangles.add(tuple(sorted([node1, node2, node3])))
    return triangles

def BronKerbosch(graph, R, P, X, cliques):
    '''
    Bron-Kerbosch algorithm to find all maximal cliques in a graph
    Uses a recursive approach to find all cliques
    '''
    if not P and not X:
        cliques.append(R)
    while P:
        node = P.pop()
        BronKerbosch(graph, R.union([node]), P.intersection(graph[node]), X.intersection(graph[node]), cliques)
        X.add(node)


if __name__ == "__main__":
    with open("inputs/day23.txt") as f:
        data = f.read().splitlines()

    connections = [line.split('-') for line in data]

    # Create a graph representation of the connections
    graph = ParseInput(connections)

    # Part 1 - Find the number of triangles containing at least one computer starting with 't'

    triangles = FindTriangles(graph)

    t_triangles = 0
    for triangle in triangles:
        if any(node.startswith('t') for node in triangle):
            t_triangles += 1
            
    print("Number of triangles containing at least one computer starting with 't':", t_triangles)

    # Part 2 - Find the password to get into the LAN party
    
    # Find the largest clique in the graph
    cliques = []
    BronKerbosch(graph, set(), set(graph.keys()), set(), cliques)
    largest_clique = max(cliques, key=len)

    # Sort the clique alphabetically and create the password
    largest_clique = sorted(largest_clique)
    password = ','.join(largest_clique)
    print("Password to get into the LAN party:", password)
