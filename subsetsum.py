def subset_sum(n, W, weights):
    # Initialize a 2D array M with dimensions (n+1) x (W+1)
    M = [[0] * (W + 1) for _ in range(n + 1)]

    # Populate the array according to the algorithm
    for w in range(W + 1):
        M[0][w] = 0

    for i in range(1, n + 1):
        M[i][0] = 0

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] > w:
                M[i][w] = M[i - 1][w]
            else:
                M[i][w] = max(M[i - 1][w], weights[i - 1] + M[i - 1][w - weights[i - 1]])

    return M[n][W]

# Take user input
n = int(input("Enter the number of items (n): "))
W = int(input("Enter the maximum weight (W): "))
weights = []

print(f"Enter the weights of {n} items:")
for i in range(n):
    weight = int(input(f"Weight {i + 1}: "))
    weights.append(weight)

# Calculate and print the result
result = subset_sum(n, W, weights)
print(f"The maximum weight sum that can be achieved is: {result}")
