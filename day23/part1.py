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

def find_triangles(graph):
    """
    Identifies all triangles (sets of three mutually connected nodes) in the graph.

    Args:
        graph (defaultdict(set)): The graph represented as an adjacency list.

    Returns:
        set of tuple: A set of tuples, each containing three nodes forming a triangle.
    """
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            common_neighbors = neighbors.intersection(graph[neighbor])
            for common in common_neighbors:
                triangle = tuple(sorted([node, neighbor, common]))
                triangles.add(triangle)
    return triangles

def filter_triangles_by_t(triangles):
    """
    Filters triangles to include only those containing at least one node that starts with 't'.

    Args:
        triangles (set of tuple): A set of triangles.

    Returns:
        list of tuple: A list of triangles meeting the criteria.
    """
    return [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]

# Example input for testing
test_input = [
    "kh-tc", "qp-kh", "de-cg", "ka-co", "yn-aq", "qp-ub", "cg-tb", "vc-aq",
    "tb-ka", "wh-tc", "yn-cg", "kh-ub", "ta-co", "de-co", "tc-td", "tb-wq",
    "wh-td", "ta-ka", "td-qp", "aq-cg", "wq-ub", "ub-vc", "de-ta", "wq-aq",
    "wq-vc", "wh-yn", "ka-de", "kh-ta", "co-tc", "wh-qp", "tb-vc", "td-yn"
]

# Build the graph from the example input
graph = build_graph(test_input)

# Find triangles and filter by 't' for the example input
example_triangles = find_triangles(graph)
example_filtered = filter_triangles_by_t(example_triangles)

# Display results for the example input
print("Example Triangles:", example_triangles)
print("Filtered Triangles:", example_filtered)
print("Count of Filtered Triangles:", len(example_filtered))

# Validate correctness using the example data
expected_filtered_count = 7
if len(example_filtered) == expected_filtered_count:
    print("Test passed! Proceeding to file input...")

    # Process the input file
    try:
        with open('input.txt', 'r') as f:
            file_input = f.read().strip().split('\n')

        # Build graph for the file input
        graph = build_graph(file_input)

        # Find triangles and filter by 't' for the file input
        file_triangles = find_triangles(graph)
        file_filtered = filter_triangles_by_t(file_triangles)

        # Display results for the file input
        print("Count of Filtered Triangles in File:", len(file_filtered))
    except FileNotFoundError:
        print("Error: input.txt not found. Please ensure the file is in the correct directory.")
else:
    print("Test failed. Please check the algorithm.")