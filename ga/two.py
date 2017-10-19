from pyeasyga import pyeasyga
from random import choice, randint

captains = ["arm", "jac", "rom", "yan"]
boats = ["dr", "fr", "sa", "wp"]
locs = ["as", "bb", "rr", "tt"]
manatees = [3, 4, 5, 6]

ga = pyeasyga.GeneticAlgorithm([], population_size=150, generations=150)

def create_individual(data):
    individual = [None] * 4
    for i in range(len(individual)):
        individual[i] = {"cap": choice(captains), "boat": choice(boats), "loc": choice(locs), "man": choice(manatees)}
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
    for k in ["cap", "boat", "loc", "man"]:
        if len(set(i[k] for i in indv)) == 4:
            fitness += 1
    #c1
    dr = get_first(indv, "boat", "dr")
    if dr and ((dr["loc"] == "rr") ^ (dr["cap"] == "rom")):
        fitness += 1
    #c2
    rr_m = get_first_v(indv, "man", "loc", "rr")
    wp_m = get_first_v(indv, "man", "boat", "wp")
    if rr_m and wp_m and rr_m < wp_m:
        fitness += 1
    #c3
    rr = get_first(indv, "loc", "rr")
    ya = get_first(indv, "cap", "yan")
    sam = get_first(indv, "boat", "sa")
    if rr and ya and sam and all_diff(rr, ya, sam):
       fitness += 1
    #c4
    bb_m = get_first_v(indv, "man", "loc", "bb")
    if rr_m and bb_m and bb_m == rr_m + 2:
        fitness += 1
    #c5
    man5 = get_first(indv, "man", 5)
    if man5 and man5["loc"] != "as":
        fitness += 1
    #c6
    man3 = get_first(indv, "man", 3)
    if man3 and ((man3["cap"] == "yan") ^ (man3["boat"] == "sa")):
        fitness += 1
    #c7
    if sam and sam["loc"] == "bb":
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
    key = choice(["cap", "boat", "loc", "man"])
    if key == "cap":
        value = choice(captains)
    if key == "boat":
        value = choice(boats)
    if key == "loc":
        value = choice(locs)
    if key == "man":
        value = choice(manatees)
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
