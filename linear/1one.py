from pulp import *

prob = LpProblem("Plane", LpMinimize)

# Ell: 0, Hen: 1, Oma: 2, Val: 3

black = LpVariable("black", 0, 3, cat=LpInteger)
blue = LpVariable("blue", 0, 3, cat=LpInteger)
pink = LpVariable("pink", 0, 3, cat=LpInteger)
silver = LpVariable("silver", 0, 3, cat=LpInteger)

d15 = LpVariable("d15", 0, 3, cat=LpInteger)
d25 = LpVariable("d25", 0, 3, cat=LpInteger)
d35 = LpVariable("d35", 0, 3, cat=LpInteger)
d45 = LpVariable("d45", 0, 3, cat=LpInteger)

#d15.setInitialValue(0)
#d25.setInitialValue(0)
#d35.setInitialValue(0)
#d45.setInitialValue(0)

ds = [d15, d25, d35, d45]
cs = [black, blue, pink, silver]    

def exists(*args):
    for v in args:
        if v == None:
            return False
    return True

def name_to_dist(i):
    return next((d for d in ds if d.value() == i), None)

def color_to_dist(c):
    return next((d for d in ds if d.value() == c.value()), None)

prob += d35 == 1
prob += silver == 1
prob.solve()
prob += pink == 2
prob.solve()
for d in ds:
    prob += d == 1
prob.solve()
#prob += name_to_dist(2) > color_to_dist(silver)
#print(name_to_dist(2), color_to_dist(silver))
#prob += exists(name_to_dist(2), color_to_dist(silver)) and name_to_dist(2) > color_to_dist(silver)
#prob += exists(name_to_dist(0), color_to_dist(black)) and name_to_dist(0) == color_to_dist(black) + 1
#prob += exists(color_to_dist(pink), color_to_dist(black)) and color_to_dist(pink) == color_to_dist(black) + 1

S = prob.solve()

print("black, blue, pink, silver") 
print(black.value(), blue.value(), pink.value(), silver.value())
print("---")
print("d15, d25, d35, d45")
print(d15.value(), d25.value(), d35.value(), d45.value())

print(S)
