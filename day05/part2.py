from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as file:
        input_text = file.read()
    sections = input_text.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
    return rules, updates

def build_graph(rules):
    graph = defaultdict(set)
    for x, y in rules:
        graph[x].add(y)
    return graph

def topological_sort(update, graph):
    in_degree = defaultdict(int)
    present_nodes = set(update)
    
    for node in present_nodes:
        for neighbor in graph[node]:
            if neighbor in present_nodes:
                in_degree[neighbor] += 1
    
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            if neighbor in present_nodes:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
    return sorted_order

def is_correctly_ordered(update, graph):
    return topological_sort(update, graph) == update

def find_middle(update):
    return update[len(update) // 2]

def solve_puzzle_part_two(file_path):
    rules, updates = parse_input(file_path)
    graph = build_graph(rules)
    
    middle_sum = 0
    for update in updates:
        if not is_correctly_ordered(update, graph):
            correct_order = topological_sort(update, graph)
            middle_sum += find_middle(correct_order)
    return middle_sum

# Solve Part Two using input from 'input.txt'
if __name__ == "__main__":
    result = solve_puzzle_part_two("input.txt")
    print(result)