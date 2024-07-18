class Graph:
    class Edge:
        def __init__(self, src, dest, weight):
            self.src = src
            self.dest = dest
            self.weight = weight

    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []  # List to store all edges

    def add_edge(self, u, v, w):
        edge = self.Edge(u, v, w)
        self.edges.append(edge)

    def bellman_ford(self, src):
        # Initialize distances from source to all other vertices as INFINITE
        if src >= self.V or src < 0:
            raise ValueError("Source index is out of bounds.")
        
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Relax all edges |V| - 1 times.
        for _ in range(self.V - 1):
            for edge in self.edges:
                u = edge.src
                v = edge.dest
                weight = edge.weight
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative-weight cycles.
        for edge in self.edges:
            u = edge.src
            v = edge.dest
            weight = edge.weight
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Print all distances
        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

if __name__ == "__main__":
    # Take user input for number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    g = Graph(num_vertices)

    for _ in range(num_edges):
        u, v, w = map(int, input("Enter edge (src dest weight): ").split())
        g.add_edge(u, v, w)

    src_vertex = int(input("Enter the source vertex: "))
    
    g.bellman_ford(src_vertex)
