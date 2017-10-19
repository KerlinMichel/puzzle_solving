from pulp import *
import pprint
pp = pprint.PrettyPrinter(indent=4)

names = ["Hen", "Ell", "Oma", "Val"]
colors = ["black", "blue", "pink", "silver"]
distances = [15, 25, 35, 45]

cls = LpVariable.dicts("cls", (names, colors), 0, 1, LpInteger)
dists = LpVariable.dicts("dists", (names, distances), 0, 1, LpInteger)

for c in colors:
    for d in distances:
        pass

prob = LpProblem("Planes", LpMinimize)

prob += 0

for c in colors:
    prob += lpSum([cls[n][c] for n in cls if cls[n][c] == 1]) == 1

for d in distances:
    prob += lpSum([dists[n][d] for n in dists if dists[n][d] == 1]) == 1

for n in names:
    #print([cls[n][c].value() for c in cls[n] if cls[n][c] == 1])
    prob += lpSum([cls[n][c] for c in cls[n] if cls[n][c] == 1]) == 1
    prob += lpSum(dists[n][d] for d in dists[n] if dists[n][d] == 1) == 1
    #for c in colors:
    #    prob += lpSum([cls[n][cl] for cl in cls[n] if cls[n][cl] == 1]) == 1
    #for d in distances:
    #    prob += lpSum([dists[n][di] for di in dists[n] if dists[n][di] == 1]) == 1

prob += dists['Hen'][35] == 1
prob += cls['Hen']['silver'] == 1

def c3():
    n = [n for n in cls if cls[n]['silver'] == 1][0]
    sd = [d for d in dists[n] if dists[n][d] == 1][0]
    return lpSum([dists['Oma'][d] for d in dists['Oma'] if dists['Oma'][d] == 1 and d > sd]) == 1

def c4():
    #ed = [d for d in dists['Ell'] if dists['Ell'][d] == 1][0]
    bn = [n for n in cls if cls[n]['black'] == 1][0]
    bd = [d for d in dists[bn] if dists[bn][d] == 1][0]
    return lpSum([dists['Ell'][d] for d in dists['Ell'] if dists['Ell'][d] == 1 and d == bd + 10]) == 1

def c5():
    pn = [n for n in cls if cls[n]['pink'] == 1][0]
    pd = [d for d in dists[pn] if dists[pn][d] == 1][0]
    bn = [n for n in cls if cls[n]['black'] == 1][0]
    return lpSum([dists[bn][d] for d in dists[bn] if dists[bn][d] == 1 and pd == d + 10]) == 1

#prob += c3()
prob += c4()
#prob += c5()
#prob += dists['Hen'][35] == 1
#prob += cls['Hen']['silver'] == 1
S = prob.solve()
print(LpStatus[S])
#pp.pprint(cls)
#pp.pprint(dists)
for n in names:
    print(n)
    print([c for c in cls[n] if cls[n][c].value() == 1][0])
    print([d for d in dists[n] if dists[n][d].value() == 1][0])
    print('---')
