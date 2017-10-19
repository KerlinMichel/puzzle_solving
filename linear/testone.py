from pulp import *

s_names = ["Hen", "Ell", "Oma", "Val"]
colors = ["black", "blue", "pink", "silver"]
distances = [15, 25, 35, 45]

cls = LpVariable.dicts("cls", colors, 0, 3, LpInteger)
dists = LpVariable.dicts("cls", distances, 0, 3, LpInteger)
names = LpVariable.dicts("cls", s_names, 0, 3, LpInteger)

prob = LpProblem("Planes", LpMaximize)
#print(sum(cls.values()))
prob += sum(cls.values()) + sum(dists.values()) + sum(names.values())

prob += names['Hen'] == 0
prob += names['Ell'] == 1
prob += names['Oma'] == 2
prob += names['Val'] == 3

prob += sum(names.values()) == 6
prob += sum(dists.values()) == 6
prob += sum(cls.values()) == 6

prob += names['Hen'] == dists[35]
prob += names['Hen'] == cls['silver']

for i,d in enumerate(distances):
    for d1 in distances[i+1:]:
        prob += dists[d] + dists[d1] <= 5

for i,c in enumerate(colors):
    for c1 in colors[i+1:]:
        prob += cls[c] + cls[c1] <= 5

print(prob)
def c3():
    #od = [d for d in dists if dists[d] == names['Oma']][0]
    #sd = [d for d in dists if od == d + 10 and dists[d] == cls['silver']][0]
    #return names['Oma'] == dists[od] and cls['silver'] == dists[sd]
    s = [d for d in dists if dists[d] == cls['silver']][0]
    return [d for d in dists if names['Oma'] == dists[d] and d > s][0] == d

#pay attention to minus signs for previous attemp
def c4():
    b = cls['black']
    b = [d for d in dists if dists[d] == b][0]
    return [dists[d] for d in dists if names['Ell'] == dists[d] and d == b + 10][0] == 1

def c5():
    p = [d for d in dists if dists[d] == cls['pink']][0]
    b = [d for d in dists if dists[d] == cls['black']][0]
    return [dists[d] for d in dists if d == b + 10][0] == cls['pink']
#prob += c3()
#prob += c4()
#prob += c5()
#prob += lpSum([dists[d] for d in dists if dists[d] == cls['pink']]) - lpSum([dists[d] for d in dists if dists[d] == cls['black']]) == 0
#print(lpSum([d for d in dists if dists[d] == cls['silver']]))
#prob += lpSum([d for d in dists if dists[d] == names['Oma']]) - lpSum([d for d in dists if dists[d] == cls['silver']])
#prob += lpSum([d for d in dists if dists[d] == cls['pink']]) - lpSum([d for d in dists if dists[d] == cls['black']]) >= 10
#prob += lpSum([d for d in dists if dists[d] == cls['black']]) - lpSum([d for d in dists if dists[d] == cls['pink']]) == -10
S = prob.solve()

print(LpStatus[S])
print([(d, dists[d].value()) for d in dists])
print([(c, cls[c].value()) for c in cls])
#print(sum([dists[d].value() for d in dists]))
for i in range(len(names)):
    print(next((n for n in names if names[n].value() == i), None))
    print(next((c for c in cls if cls[c].value() == i), None))
    print(next((d for d in dists if dists[d].value() == i), None))
    print('---')
