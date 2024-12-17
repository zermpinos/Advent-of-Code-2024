grid = {
    i + j * 1j: c  # i + j * 1j gives a complex number representing the grid position (i, j)
    for i, r in enumerate(open('input.txt'))  # Iterate over each line in the file, where 'i' is the row index.
    for j, c in enumerate(r.strip())  # Iterate over each character 'c' in the row, where 'j' is the column index.
}

# Find the starting position by looking for the '^' character in the grid.
start = min(
    p for p in grid if grid[p] == '^')

# Define the `walk` function, which simulates movement on the grid.
def walk(grid):
    pos, direction, seen = start, -1, set()  # Initialize starting position, direction, and the set of seen states.

    # Continue walking while the current position is in the grid and we haven't revisited the same position in the same direction.
    while pos in grid and (pos, direction) not in seen:
        seen.add((pos, direction))  # Mark the current position and direction as visited to avoid revisiting.

        # If the next position in the current direction is an obstacle ('#'), change direction.
        # The direction is multiplied by -1j to rotate it 90 degrees (90 degrees clockwise in the complex plane).
        if grid.get(pos + direction) == "#":
            direction *= -1j  # Rotate the direction 90 degrees to the right.
        else:
            pos += direction  # Move to the next position in the current direction.

    # Return the set of visited positions and whether the walk revisited any position.
    return {p for p, _ in seen}, (pos, direction) in seen


# Call the `walk` function and get the result.
path, revisited = walk(grid)

# Output the length of the path and the number of times a position was revisited during the walk.
# The path length is simply the number of unique positions visited.
# The second part counts how many times a position was revisited by making a walk on each position in the path
# and checking if the walk revisits any position.
print(len(path), sum(walk(grid | {o: '#'})[1] for o in path))
