#This is sample code quiz
import random

def generate():
    testcases = []
    for i in range(20):
        n = random.randint(9700, 13000)
        alpha = list(generate_DNA(2))
        betta = list(generate_DNA(5))
        query = alpha + betta + alpha
        database = []
        while len(database) < n - 7:
            if random.randint(0, 3) == 0:
                database += alpha + betta
            else:
                database += random.choice('ACGT')
        database = ''.join(database[:n])
        query = ''.join(query)
        testcases.append('%s\n%s' % (query, database))
    return testcases

def generate_DNA(n):
    return ''.join([random.choice('ACGT') for i in range(n)])

def solve(dataset):
    pattern = dataset.splitlines()[0]
    data = dataset.splitlines()[1]
    
    k = len(pattern)
    return str(sum([pattern == data[i:i+k] for i in range(len(data))]))


def check(reply, clue):
    return int(reply) == int(clue)

tests = [
     ("ATA\nATATA", "2", "2")        
]