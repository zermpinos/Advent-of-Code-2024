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

# Flatten the second_half list into a single list of values
flattened_second_half = sum(second_half, [])

for sublist in reversed(first_half):
    for idx in reversed(range(len(sublist))):
        if flattened_second_half and sublist[idx] > flattened_second_half[0]:
            sublist[idx] = flattened_second_half[0]
            flattened_second_half = flattened_second_half[1:]

result = sum(i * j for i, sublist in enumerate(first_half) for j in sublist)

print(result)
