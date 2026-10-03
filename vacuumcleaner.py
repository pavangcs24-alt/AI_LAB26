

# Simple Vacuum Cleaner with Multiple Rooms

# Get number of rooms
n = int(input("Enter number of rooms: "))

rooms = []

# Get room conditions from user
for i in range(n):
    condition = input(f"Is room {i + 1} dirty or clean? ").lower()

    if condition == "dirty":
        rooms.append("Dirty")
    else:
        rooms.append("Clean")

# Get starting position
position = int(input(f"Enter starting room (1-{n}): ")) - 1

print("\nStarting the vacuum cleaner...\n")

# Visit every room
for i in range(n):
    print(f"Vacuum is in Room {position + 1}")

    if rooms[position] == "Dirty":
        print("Room is dirty. Cleaning...")
        rooms[position] = "Clean"
    else:
        print("Room is already clean.")

    # Move to the next room
    if position < n - 1:
        position += 1

    print()

print("All rooms have been cleaned!")

# Display final state
print("Final room status:")
for i in range(n):
    print(f"Room {i + 1}: {rooms[i]}")