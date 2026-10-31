
N = 4

# Heuristic: Count number of attacking pairs
def heuristic(state):
    cost = 0

    for i in range(N):
        for j in range(i + 1, N):
            # Check diagonal attack
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


# Generate 6 neighbours by swapping indices
def get_neighbors(state):
    neighbors = []

    for i in range(N):
        for j in range(i + 1, N):
            new_state = state.copy()

            # Swap two positions
            new_state[i], new_state[j] = new_state[j], new_state[i]

            neighbors.append(new_state)

    return neighbors


# Hill Climbing Algorithm
def hill_climbing(state):

    while True:
        current_cost = heuristic(state)

        print("\nCurrent State:", state)
        print("Current Cost:", current_cost)

        if current_cost == 0:
            print("Solution Found!")
            return state

        neighbors = get_neighbors(state)

        print("\nAll 6 Neighbours:")

        for k, neighbor in enumerate(neighbors):
            print(k + 1, neighbor,
                  "Cost =", heuristic(neighbor))

        # Select minimum cost neighbour
        best_neighbor = min(neighbors, key=heuristic)
        min_cost = heuristic(best_neighbor)

        print("\nMinimum Cost:", min_cost)
        print("Best Neighbour:", best_neighbor)

        # Stop if no improvement
        if min_cost >= current_cost:
            print("Local Minimum Reached!")
            return None

        state = best_neighbor


# User input
print("Enter 4 queen positions (0 to 3):")

state = []

for i in range(N):
    x = int(input("Enter x" + str(i) + ": "))
    if x < 0 or x >= N or x in state:
        print("Invalid input! Enter unique values from 0 to 3.")
        exit()
    state.append(x)

# Run algorithm
solution = hill_climbing(state)

if solution:
    print("\nFinal Solution:", solution)
    print("Final Cost:", heuristic(solution))
