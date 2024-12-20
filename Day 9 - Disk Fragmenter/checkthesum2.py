first_half = []
second_half = []
current_value = 0

with open('input.txt') as file:
    content = file.read().strip()

for index, char in enumerate(content):
    range_end = current_value + int(char)
    new_range = list(range(current_value, range_end))
    if index % 2 == 0:
        first_half.append(new_range)
    else:
        second_half.append(new_range)

    current_value = range_end

# Process second_half to try to match ranges from first_half
for y in reversed(range(len(first_half))):
    for x in range(len(second_half)):
        if len(second_half[x]) >= len(first_half[y]) and first_half[y][0] > second_half[x][0]:
            first_half[y] = second_half[x][:len(first_half[y])]
            second_half[x] = second_half[x][len(first_half[y]):]

result = sum(i * j for i, sublist in enumerate(first_half) for j in sublist)

print(result)
