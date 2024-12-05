def load_data(name: str) -> list[list[int]]:
    with open(name, 'r') as f:
        return [list(map(int, line.split())) for line in f.readlines()]


def is_valid(integer: list[int]) -> bool:
    for i in range(len(integer)-1):
        if integer[i] - integer[i+1] <= 0:
            return False
    return all(1 <= integer[i] - integer[i + 1] <= 3 for i in range(len(integer) - 1))

def count_valid_permutations(list_of_lists: list[list[int]]) -> int:
    valid_count = 0
    for integers in list_of_lists:
        # Check both original and reversed lists
        if is_valid(integers) or is_valid(integers[::-1]):
            valid_count += 1

    return valid_count


filename = 'input.txt'
data = load_data(filename)
print(f"Total number of valid permutations: {count_valid_permutations(data)}")
