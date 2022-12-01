with open('input', 'r') as f:
    elf_carrying = 0
    max_carrying = 0
    line = f.readline()
    while line:
        if line != '\n':
            elf_carrying += int(line)
        else:
            if elf_carrying > max_carrying:
                max_carrying = elf_carrying
            elf_carrying = 0

        line = f.readline()

    print(max_carrying)