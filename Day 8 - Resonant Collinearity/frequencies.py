# Open the input file and create a dictionary where keys are complex numbers (p + q*1j), and values are characters from the file.
data_dict = {
    (p + q * 1j): i  # Key: complex number (p + q * 1j), Value: character from the file
    for p, line in enumerate(open("input.txt"))
    for q, i in enumerate(line.strip())
}


def process_data(d):
    result = []
    for r in [[2], range(51)]:
        result.append(
            len(set(
                i + k * (j - i)
                for i in d for j in d
                if i != j and d[i] == d[j] != "."
                for k in r
                if i + k * (j - i) in d)))

    return result

result = process_data(data_dict)

print(result)
