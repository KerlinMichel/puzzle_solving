from pyeasyga import pyeasyga
from random import choice, randint

cars = ['cav', 'fie', 'gra', 'inj']
lps = ['fr', 'gg', 'mr', 'yg']
states = ['al', 'co', 'ha', 'lo']
fines = [25, 50, 75, 100]

ga = pyeasyga.GeneticAlgorithm([])

def create_individual(data):
    individual = [None] * 4
    for i in range(len(individual)):
        individual[i] = {"car": choice(cars), "lp": choice(lps), "st": choice(states), "fine": choice(fines)}
    return individual

ga.create_individual = create_individual

def get_first(l, key, val):
    return next((i for i in l if i[key] == val), None)

def get_first_v(l, get_v, key, val):
    return next((i[get_v] for i in l if i[key] == val), None)

def all_diff(*args):
    return len([dict(t) for t in set(tuple(d.items()) for d in args)]) == len(args)

def fit(indv, data):
    fitness = 0
    for k in ["car", "lp", "st", "fine"]:
        if len(set(i[k] for i in indv)) == 4:
            fitness += 1
    #c1
    yg = get_first(indv, "lp", "yg")
    haw = get_first(indv, "st", "ha")
    if yg and haw and yg["fine"] == haw["fine"] + 25:
        fitness += 1
    #c2
    fie = get_first(indv, "car", "fie")
    gg = get_first(indv, "lp", "gg")
    if fie and gg and fie["fine"] < gg["fine"]:
        fitness += 1
    #c3
    cav = get_first(indv, "car", "cav")
    if cav and cav["st"] == "co":
        fitness += 1
    #c4
    f50 = get_first(indv, "fine", 50)
    gra = get_first(indv, "car", "gra")
    inj = get_first(indv, "car", "inj")
    if f50 and gra and inj and all_diff(f50, gra, inj):
        fitness += 1
    #c5
    al = get_first(indv, "st", "al")
    if al and fie and al["fine"] == fie["fine"]:
        fitness += 1
    #c6
    fr = get_first(indv, "lp", "fr")
    if gra and fr and gra["fine"] > fr["fine"]:
        fitness += 1
    #c7
    f100 = get_first(indv, "fine", 100)
    if f100 and f100["lp"] != "gg":
        fitness += 1
    return fitness

def crossover(parent_1, parent_2):
    i = randint(0, 3)
    j = randint(0, 3)
    child_1 = parent_1
    child_2 = parent_2
    p = child_1[i]
    child_1[i] = child_2[j]
    child_2[j] = p
    return child_1, child_2

def mutate(individual):
    i = randint(0, 3)
    key = choice(["car", "lp", "st", "fine"])
    if key == "car":
        value = choice(cars)
    if key == "lp":
        value = choice(lps)
    if key == "st":
        value = choice(states)
    if key == "fine":
        value = choice(fines)
    individual[i][key] = value

ga.fitness_function = fit
ga.crossover_function = crossover
ga.mutate_function = mutate
ga.run()
bestf, best = ga.best_individual()
while bestf < 11:
    ga.run()
    bestf, best = ga.best_individual()
bestf, best = ga.best_individual()
print(bestf)
for i in best:
    print(i)

