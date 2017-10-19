from pyeasyga import pyeasyga
from random import choice, randint

drugs = ['biz', 'dam', 'fav', 'gra']
conds = ['df', 'di', 'hd', 'in']
srcs = ['be', 'br', 'fr', 'mu']
months = [1, 2, 3, 4]

ga = pyeasyga.GeneticAlgorithm([])

def create_individual(data):
    individual = [None] * 4
    for i in range(len(individual)):
        individual[i] = {"drug": choice(drugs), "cond": choice(conds), "src": choice(srcs), "month": choice(months)}
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
    for k in ["drug", "cond", "src", "month"]:
        if len(set(i[k] for i in indv)) == 4:
            fitness += 1
    #c1
    mu = get_first(indv, "src", "mu")
    if mu and mu["cond"] == "hd":
        fitness += 1
    #c2
    be = get_first(indv, "src", "be")
    if be and be["cond"] == "df":
        fitness += 1
    #c3
    hd = get_first(indv, "cond", "hd")
    if hd and be and ((hd["drug"] == "dam" and be["month"] == 3) ^ (hd["month"] == 3 and be["drug"] == "dam")):
        fitness += 1
    #c4
    fav = get_first(indv, "drug", "fav")
    di = get_first(indv, "cond", "di")
    if fav and di and fav["month"] == di["month"] + 2:
        fitness += 1
    #c5
    ap = get_first(indv, "month", 4)
    br = get_first(indv, "src", "br")
    if ap and di and br and all_diff(ap, di, br):
        fitness += 1
    #c6
    gra = get_first(indv, "drug", "gra")
    if gra and ((gra["month"] == 3) ^ (gra["src"] == "br")):
        fitness += 1
    #c7
    if fav and fav["src"] != "be":
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
    key = choice(["drug", "cond", "src", "month"])
    if key == "drug":
        value = choice(drugs)
    if key == "cond":
        value = choice(conds)
    if key == "src":
        value = choice(srcs)
    if key == "month":
        value = choice(months)
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

