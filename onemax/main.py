import numpy as np

def fitness(population):
    score = np.sum(population, axis=1)
    return score

def selection(population, scores):
    tournament = np.random.choice(len(population), size=(len(population), 2))

    winner_tournament = np.argmax(scores[tournament], axis=1)
    
    selected = tournament[np.arange(len(population)), winner_tournament]

#    selected = []
#    for i in range(0, len(population)):
#        tournament = np.random.choice(len(population), size=2, replace=False)
#        if (scores[tournament[0]] > scores[tournament[1]]):
#            selected.append(tournament[0])
#        else:
#            selected.append(tournament[1])

    return population[selected]

def crossover(parents):
    half = len(parents) // 2
    parents_a = parents[:half]
    parents_b = parents[half:]

    cross = np.random.randint(low=1, high=4)

    childs_1 = []
    for i in range(0, half):
        childs_1.append(np.concatenate((parents_a[i][:cross], parents_b[i][cross:])))
    
    childs_2 = []
    for i in range(0, half):
        childs_2.append(np.concatenate((parents_b[i][:cross], parents_a[i][cross:])))

    return childs_1 + childs_2

population = np.random.randint(low=0, high=2, size=(10, 5))

scores = fitness(population)

selected = selection(population, scores)

print(crossover(selected))