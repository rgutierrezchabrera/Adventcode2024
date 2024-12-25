from collections import defaultdict

def build_graph(connections):
    """
    Parses the input connections and constructs an undirected graph.

    Args:
        connections (list of str): List of connections, each formatted as "node1-node2".

    Returns:
        defaultdict(set): A graph represented as an adjacency list.
    """
    graph = defaultdict(set)
    for connection in connections:
        a, b = connection.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def bron_kerbosch(R, P, X, graph, cliques):
    """
    Implements the Bron-Kerbosch algorithm to find all maximal cliques in a graph.

    Args:
        R (set): Current clique.
        P (set): Candidates for inclusion in the clique.
        X (set): Nodes already excluded from the clique.
        graph (defaultdict(set)): The graph represented as an adjacency list.
        cliques (list of set): A list to store all maximal cliques.
    """
    if not P and not X:
        cliques.append(R)
        return

    for node in list(P):
        bron_kerbosch(
            R.union({node}),
            P.intersection(graph[node]),
            X.intersection(graph[node]),
            graph,
            cliques
        )
        P.remove(node)
        X.add(node)

def find_largest_clique(graph):
    """
    Finds the largest clique in the graph using the Bron-Kerbosch algorithm.

    Args:
        graph (defaultdict(set)): The graph represented as an adjacency list.

    Returns:
        set: The largest clique in the graph.
    """
    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    largest_clique = max(cliques, key=len)
    return largest_clique

# Example input for testing
test_input = [
    "kh-tc", "qp-kh", "de-cg", "ka-co", "yn-aq", "qp-ub", "cg-tb", "vc-aq",
    "tb-ka", "wh-tc", "yn-cg", "kh-ub", "ta-co", "de-co", "tc-td", "tb-wq",
    "wh-td", "ta-ka", "td-qp", "aq-cg", "wq-ub", "ub-vc", "de-ta", "wq-aq",
    "wq-vc", "wh-yn", "ka-de", "kh-ta", "co-tc", "wh-qp", "tb-vc", "td-yn"
]

# Build the graph from the example input
graph = build_graph(test_input)

# Find the largest clique
largest_clique = find_largest_clique(graph)

# Generate the password
password = ",".join(sorted(largest_clique))

# Display results for the example input
print("Largest Clique:", largest_clique)
print("Password:", password)

# Process the input file
try:
    with open('input.txt', 'r') as f:
        file_input = f.read().strip().split('\n')

    # Build graph for the file input
    graph = build_graph(file_input)

    # Find the largest clique for file input
    largest_clique = find_largest_clique(graph)

    # Generate the password for file input
    password = ",".join(sorted(largest_clique))

    # Display the password for the LAN Party
    print("Password for the LAN Party:", password)
except FileNotFoundError:
    print("Error: input.txt not found. Please ensure the file is in the correct directory.")