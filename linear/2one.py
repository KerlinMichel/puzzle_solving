from pulp import *

#          1      2      3     4
names = ["Hen", "Ell", "Oma", "Val"]
colors = ["black", "blue", "pink", "silver"]
distances = [15, 25, 35, 45]

prob = LpProblem("Planes", LpMinimize)

cls = LpVariable.dicts("cls", colors, 0, 3, LpInteger)
dists = LpVariable.dicts("dists", distances, 0, 3, LpInteger)

prob += 0

#for d in distances:
#    prob += lpSum(dists[d]) == 2, ""

#for i in range(len(names)):
#    for d in distances:
#        prob += dists[d] == 1

prob += dists[35] == 1
prob += cls['silver'] == 1
#prob += cls['black'] == 1

#print([d for d in dists if dists[d].value() == i])

for i in range(len(names)):
    prob += lpSum([d for d in dists]) == 1

for i in range(len(names)):
    prob += lpSum([c for c in cls]) == 1

#prob += len(set(list([dists[d].value() for d in dists]))) == 4
#print(dists)
#c = combination(list([dists[d].value() for d in dists]), 4)
#for i in c:
#    print(i)
S = prob.solve()
print(S)
print([(d, dists[d].value()) for d in dists])
print('---')
print([(c, cls[c].value()) for c in cls])

#for d in dists:
#    print(d)
#    print(dists[d].value())
