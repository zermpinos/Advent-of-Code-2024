with open("input.txt") as file:
    data = file.read().split("mul(")

multiplication1, multiplication2 = 0, 0

activate = True # Flag variable to track whether we are in the 'do()' or 'don't()' sequence

for sequence in data:
    sequence_parse = sequence.split(",", 1)
    value1 = sequence_parse[0]

    if value1.isdigit():
        value2 = sequence_parse[1].split(")")[0]
        if value2.isdigit():
            multiplication1 += int(value1)*int(value2)
            if activate: multiplication2 += int(value1)*int(value2)

    # Check which direction of comparison is more frequent
    if sequence.find("don't()") > sequence.find("do()"): activate = False
    if sequence.find("do()") > sequence.find("don't()"): activate = True


print(multiplication1, multiplication2)
