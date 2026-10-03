def dls(state, goal, depth, path, visited):

    # Goal test
    if state == goal:
        return path

    # Depth limit reached
    if depth == 0:
        return None

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = []

    if row > 0:
        moves.append(("UP", zero - 3))

    if row < 2:
        moves.append(("DOWN", zero + 3))

    if col > 0:
        moves.append(("LEFT", zero - 1))

    if col < 2:
        moves.append(("RIGHT", zero + 1))

    for operation, move in moves:

        new = list(state)

        # Swap blank with tile
        new[zero], new[move] = new[move], new[zero]

        new = tuple(new)

        # Avoid repeated states
        if new not in visited:

            visited.add(new)

            result = dls(
                new,
                goal,
                depth - 1,
                path + [(operation, new)],
                visited
            )

            if result is not None:
                return result

            # Remove while backtracking
            visited.remove(new)

    return None


# ---------- IDS ----------

def ids(start, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        visited = {start}

        result = dls(
            start,
            goal,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

        depth += 1


# ---------- USER INPUT ----------

print("Enter the 8-puzzle matrix (0 for blank):")

matrix = []

for i in range(3):
    matrix.append(
        list(map(int, input().split()))
    )


# Convert matrix to tuple
start = tuple(
    num
    for row in matrix
    for num in row
)


# Goal state
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# ---------- SOLVE USING IDS ----------

solution = ids(start, goal)


# ---------- PRINT SOLUTION ----------

if solution:

    print("\nSolution path:\n")

    for depth, (operation, state) in enumerate(solution, start=1):

        print("Depth:", depth)
        print("Operation:", operation)

        for i in range(0, 9, 3):
            print(state[i:i + 3])

        print()

else:

    print("No solution found.")
