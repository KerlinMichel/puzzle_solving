from pyeasyga import pyeasyga
from random import choice, randint

names = ["Hen", "Ell", "Oma", "Val"]
colors = ["black", "blue", "pink", "silver"]
distances = [15, 25, 35, 45]

ga = pyeasyga.GeneticAlgorithm([])

def create_individual(data):
    individual = [None] * 4
    for i in range(len(individual)):
        individual[i] = {"name": choice(names), "color": choice(colors), "dist": choice(distances)}
    return individual

ga.create_individual = create_individual

def exists(l):
    return len(l) > 0

def get_first(l, get_v, key, val):
    return next((i[get_v] for i in l if i[key] == val), None)

def fit(i, data):
    fitness = 0
    if type(i[0]) == dict:
        if len([p for p in i if type(p) != dict]) > 0:
            return 0
        if len(set([p['name'] for p in i])) == 4:
            fitness += 1
        if len(set([p['color'] for p in i])) == 4:
            fitness += 1
        if len(set([p['dist'] for p in i])) == 4:
            fitness += 1
        if exists([p for p in i if p["name"] == "Hen" and p["dist"] == 35]):
            fitness += 1
        if exists([p for p in i if p["name"] == "Hen" and p["color"] == "silver"]):
            fitness += 1
        oma_d = get_first(i, "dist", "name", "Oma")
        sil_d = get_first(i, "dist", "color", "silver")
        if oma_d and sil_d and oma_d > sil_d:
            fitness += 1
        ell_d = get_first(i, "dist", "name", "Ell")
        bla_d = get_first(i, "dist", "color", "black")
        if ell_d and bla_d and ell_d == bla_d + 10:
            fitness += 1
        pin_d = get_first(i, "dist", "color", "pink")
        if pin_d and bla_d and pin_d == bla_d + 10:
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
    key = choice(["name", "color", "dist"])
    if key == "name":
        value = choice(names)
    if key == "color":
        value = choice(colors)
    if key == "dist":
        value = choice(distances)
    individual[i][key] = value

ga.crossover_function = crossover
ga.mutate_function = mutate
ga.fitness_function = fit
ga.run()
bestf, best = ga.best_individual()
while bestf < 8:
    ga.run()
    bestf, best = ga.best_individual()
print(bestf)
for i in best:
    print(i)
