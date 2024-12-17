from operator import add, mul

data = [list(map(int, line.replace(':','').split())) for line in open('input.txt')]

def concatenation(number_1, number_2): return int(f"{number_1}{number_2}")

def solve(numbers, operators):
    if len(numbers) == 2:
        return numbers[0] == numbers[1]

    # Split the input list into the initial values, variable names, and remaining numbers.
    total, number_1, number_2, *rest = numbers

    for operator in operators:
        if solve([total, operator(number_1, number_2)] + rest, operators):
            return total
    return 0

print(sum(solve(numbers, operators=[add, mul]) for numbers in data))
print(sum(solve(numbers, operators=[add, mul, concatenation]) for numbers in data))
