import re

rules, part1, part2 = [], [], []

with open("input.txt") as file:
    for line in file:
        data = line.rstrip()

        if "|" in data:
            rules.append(data.split("|"))

        elif "," in data:
            passing = True
            for rule in rules:
                if re.search(r"" + rule[1] + ".+" + rule[0], data):
                    passing = False
                    break

            if passing:
                result= data.split(",")
                part1.append(int(result[len(result) // 2]))

            else:
                while True:
                    passing = True
                    for rule in rules:
                        match = re.search(r"(" + rule[1] + r").+(" + rule[0] + r")", data)
                        if match:
                            passing = False
                            data_array = data.split(",")
                            temporary = data_array[match.span(1)[0] // 3]
                            data_array[match.span(1)[0] // 3] = data_array[match.span(2)[0] // 3]
                            data_array[match.span(2)[0] // 3] = temporary
                            data = ",".join(data_array)
                    if passing:
                        break
                result= data.split(",")
                part2.append(int(result[len(result) // 2]))

print(sum(part1), sum(part2))
