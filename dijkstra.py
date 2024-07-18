import heapq

def dijkstra(graph, start, n):
    distances = [float('inf')] * n  # Initialize distances to infinity
    distances[start] = 0  # Distance to the start node is 0
    priority_queue = [(0, start)]  # Initialize the priority queue with the start node

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # Get the node with the smallest distance

        # If the distance is not the shortest known distance, skip processing
        if current_distance > distances[current_node]:
            continue

        # Update distances to neighboring nodes
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Function to read user input for the graph
def get_user_input():
    n = int(input("Enter the number of nodes: "))
    graph = [[] for _ in range(n)]
    edges_count = int(input("Enter the number of edges: "))
    
    print("Enter the edges in the format 'u v w' where u and v are nodes and w is the weight:")
    for _ in range(edges_count):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    start_node = int(input("Enter the start node: "))
    return graph, start_node, n

# Get user input
graph, start_node, n = get_user_input()

# Solve the shortest path problem using Dijkstra's algorithm
distances = dijkstra(graph, start_node, n)
print(f"Shortest distances from node {start_node}: {distances}")
