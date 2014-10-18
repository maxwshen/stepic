#This is sample dataset quiz
import random, copy

standard_mass = {'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'Y': 163,
        'W': 186}

def cyclo_peptide_spectrum(peptide, mass_table=standard_mass):
    acc_m = list(accum_mass(peptide+peptide[:-1], mass_table=mass_table))
    l = len(peptide)
    result = [0, acc_m[l]]
    for i in range(1,l):
        for j in range(l):
            result.append(acc_m[j+i] - acc_m[j])
    return sorted(result)

def accum_mass(peptide, mass_table=standard_mass):
    s = 0
    yield s
    for p in peptide:
        s += mass_table[p]
        yield s

def generate_protein(n):
    aminoacids = 'ACDEFGHKLMNPRSTVWYIQ'
    return ''.join([random.choice(aminoacids) for i in range(n)])
        
def generate():
    n = random.randint(35, 50)
    protein = generate_protein(n)
    protein2 = list(copy.copy(protein))
    num_changes = random.randint(7, 11)

    aminoacids = 'ACDEFGHKLMNPRSTVWYIQ'
    for i in range(num_changes):
        protein2[random.randint(0, len(protein2) - 1)] = random.choice(aminoacids)

    protein2_spectrum = ' '.join([str(s) for s in cyclo_peptide_spectrum(''.join(protein2))])
    return str(protein) + '\n' + protein2_spectrum

def solve(dataset):
    protein = dataset.splitlines()[0]
    spectrum = [int(s) for s in dataset.splitlines()[1].split()]
    return str(cyclo_peptide_scoring(protein, spectrum))

def cyclo_peptide_scoring(peptide, spectrum):
    spectrum2 = cyclo_peptide_spectrum(peptide)
    score = 0
    for item in spectrum:
        if item in spectrum2:
            score += 1
            del spectrum2[spectrum2.index(item)]
    return score

def check(reply, clue):
    return int(reply) == int(clue)

tests = [
    ('LFQN\n0 113 114 128 129 227 242 242 257 355 356 370 371 484', '7', '7')
]