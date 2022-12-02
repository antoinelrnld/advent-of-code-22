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

score = 0

def result(a, b):
    if (points[a] % 3 + 1) == points[b]:
        return points['win']
    if (points[b] % 3 + 1) == points[a]:
        return points['loss']
    return points['draw']


with open('input', 'r') as f:
    line = f.readline()
    while line:
        opponent, me = line.strip().split(' ')

        score += points[me] + result(opponent, me)

        line = f.readline()

    print(score)