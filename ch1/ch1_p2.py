with open('input', 'r') as f:
    elf_carrying = 0
    max_carryings = [0, 0, 0]

    line = f.readline()
    while line:
        if line != '\n':
            elf_carrying += int(line)
        else:
            max_carryings.sort()
            if elf_carrying > max_carryings[0]:
                max_carryings[0] = elf_carrying
            elf_carrying = 0


        line = f.readline()

    print(sum(max_carryings))