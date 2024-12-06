f = open("input.txt", "r")

# Initialize an empty list to store the lines of the file
file_lines = []

# Create a list to represent the 2x2 window, initialized with empty strings
window = [''] * 2

# Initialize a variable to count the occurrences of 'MAS' and 'SAM'
total = 0

for i in f:
    file_lines.append(i.strip())

# Create a string of 'Z's with length equal to twice the length of the first line
z_string = 'Z' * (len(file_lines[0]) + 2)

# Pad each line of the input data with 'Z's on either side
for i in range(len(file_lines)):
    file_lines[i] = 'Z' + file_lines[i] + 'Z'

# Add three padding lines at the top and bottom of the data
for i in range(3):
    file_lines.insert(0, z_string)
    file_lines.append(z_string)

for y in range(len(file_lines)):
    for x in range(len(file_lines[y])):
        # Check if the current cell is 'A'
        if file_lines[y][x] == 'A':

            # Calculate the middle cell of the window
            window[0] = file_lines[y - 1][x - 1] + file_lines[y][x] + file_lines[y + 1][x + 1]
            window[1] = file_lines[y + 1][x - 1] + file_lines[y][x] + file_lines[y - 1][x + 1]

            # Check if the window contains 'MAS' or 'SAM'
            if window.count('MAS') + window.count('SAM') == 2:
                total += 1

print(total)
