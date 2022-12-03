def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - 96
    return ord(c) - 38

total_priotity = 0

with open('input', 'r') as f:
    line = f.readline().strip()

    while line:
        first_half = set(line[:len(line)//2])
        second_half = set(line[len(line)//2:])

        commmon_letter = first_half.intersection(second_half)

        total_priotity += priority(list(commmon_letter)[0])

        line = f.readline().strip()

    print(total_priotity)