def kruskal_simple(graph, num_nodes):
    # Sort the edges in order of increasing cost
    sorted_edges = sorted(graph, key=lambda edge: edge[2])

    # Initially, the set T is empty
    T = []

    # Create an array to store the component id of each node
    component = list(range(num_nodes))

    def find_component(v):
        return component[v]

    # For each edge (v, w) in the sorted order
    for edge in sorted_edges:
        u, v, weight = edge
        # If u and v are in different components, add the edge to T
        if find_component(u) != find_component(v):
            T.append(edge)
            old_component = component[u]
            new_component = component[v]
            # Update the component ids
            for i in range(num_nodes):
                if component[i] == old_component:
                    component[i] = new_component

    # Return the set of edges T
    return T

# Driver code
def main():
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    
    graph = []
    for _ in range(num_edges):
        u, v, weight = map(int, input("Enter edge (u v weight): ").split())
        graph.append([u, v, weight])
    
    # Function call
    mst = kruskal_simple(graph, num_nodes)
    print("Following are the edges in the constructed MST")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

if __name__ == "__main__":
    main()
