import numpy as np


def load_grid(filename):
    with open(filename, 'r') as file:
        return np.array([[int(c) for c in line.strip()] for line in file])


grid = load_grid('input.txt')


def explore_region(position, visited, height=0, grid=None, part=1):
    i, j = position
    if grid[i, j] == height:
        if height < 9 or (part == 1 and position in visited):
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            return sum(explore_region(neighbor, visited, height + 1, grid, part)
                       for neighbor in neighbors if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1])
        visited.add(position)
        return 1
    return 0


def find_zero_positions(grid):
    return [(i, j) for i in range(grid.shape[0]) for j in range(grid.shape[1]) if grid[i, j] == 0]


def solve(grid, part):
    zero_positions = find_zero_positions(grid)
    return sum(explore_region(pos, set(), part=part, grid=grid) for pos in zero_positions)


for part in [1, 2]:
    print(solve(grid, part))
