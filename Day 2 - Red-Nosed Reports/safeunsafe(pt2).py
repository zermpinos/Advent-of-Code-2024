data = [[*map(int, l.split())] for l in open('input.txt')]

def passing(checked_list, s=0):
    for i in range(len(checked_list)-1):
        if not 1 <= checked_list[i]-checked_list[i+1] <= 3:
            return s and any(passing(checked_list[j-1:j] + checked_list[j+1:]) for j in (i,i+1))
    return True

for z in 0, 1:
    total_passing = sum(
        passing(checked_list, z) or passing(checked_list[::-1], z)
        for checked_list in data
    )

print(f"Total passing sequences: {total_passing}")
