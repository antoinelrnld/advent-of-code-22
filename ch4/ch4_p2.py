overlaps = 0

with open('input', 'r') as f:
    line = f.readline()

    while line:
        elf1, elf2 = line.split(',')
        low1, max1 = list(map(int, elf1.split('-')))
        low2, max2 = list(map(int, elf2.split('-')))

        if (low1 <= low2 and max1 >= low2) or (low2 <= low1 and max2 >= low1):
            overlaps += 1

        line = f.readline()

print(overlaps)