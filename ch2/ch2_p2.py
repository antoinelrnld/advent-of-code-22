points = {
    'A': 1,  # Pierre
    'X': 1,  # Pierre
    'B': 2,  # Feuille
    'Y': 2,  # Feuille
    'C': 3,  # Ciseaux
    'Z': 3,  # Ciseaux
    'loss': 0,
    'draw': 3,
    'win': 6
}

goal = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
}

score = 0

def move(a, b):
    if goal[b] == 'loss':
        return 3 - ((1 - points[a]) % 3)
    if goal[b] == 'win':
        return points[a] % 3 + 1
    return points[a]


with open('input', 'r') as f:
    line = f.readline()
    while line:
        opponent, gol = line.strip().split(' ')

        score += move(opponent, gol) + points[goal[gol]]

        line = f.readline()

    print(score)