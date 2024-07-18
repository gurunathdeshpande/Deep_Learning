# Function to solve the Knapsack problem
def knapsack(weights, values, capacity):
    # Number of items
    n = len(weights)

    # Create a 2D array dp where dp[i][j] represents the maximum value that can be attained with weight less than or equal to j using items up to i
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0  # If no items or weight capacity is 0, the value is 0
            elif weights[i-1] <= w:
                # Take the maximum of including the current item or not including it
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                # If the weight of the current item is more than the current capacity, do not include the item
                dp[i][w] = dp[i-1][w]

    # The last cell of dp array will hold the maximum value that can be attained with the given capacity
    return dp[n][capacity]

# User input for weights, values and capacity
weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))
values = list(map(int, input("Enter the values of the items separated by space: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

# Solve the Knapsack problem and print the result
max_value = knapsack(weights, values, capacity)
print(f"The maximum value that can be obtained is: {max_value}")
