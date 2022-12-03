def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - 96
    return ord(c) - 38

total_priotity = 0

with open('input', 'r') as f:
    line = f.readline().strip()

    while line:
        first_line = set(line)
        second_line = set(f.readline().strip())
        third_line = set(f.readline().strip())

        common_letter = first_line.intersection(second_line).intersection(third_line)
        
        total_priotity += priority(list(common_letter)[0])

        line = f.readline().strip()

    print(total_priotity)