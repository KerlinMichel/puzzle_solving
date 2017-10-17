from constraint import *
problem = Problem()

names = ["Hen", "Ell", "Oma", "Val"]
colors = ["black", "blue", "pink", "silver"]
distance = [15, 25, 35, 45]

def generate_domains():
    domain = []
    for c in colors:
        for d in distance:
            domain.append({"c": c, "d": d})
    return domain

domain = generate_domains()

for name in names:
    problem.addVariable(name, domain)

problem.addConstraint(lambda h: h["d"] == 35, ("Hen",))
problem.addConstraint(lambda h: h["c"] == 'silver', ("Hen",))

def c1(o, *args):
    for i in args:
        if i["c"] == 'silver' and o["d"] > i["d"]:
            return True
    return False

def c2(e, *args):
    for i in args:
        if i["c"] == 'black' and e["d"] == i["d"] + 10:
            return True
    return False

def c3(*args):
    pinkp = None
    blackp = None
    for i in args:
        if i["c"] == 'pink':
            pinkp = i
        if i["c"] == 'black':
            blackp = i
    return pinkp and blackp and pinkp["d"] == blackp["d"] + 10

def c4(*args):
    return len(set([p["c"] for p in args])) == 4 

def c5(*args):
    return len(set([p["d"] for p in args])) == 4

problem.addConstraint(c1, ("Oma", "Ell", "Hen", "Val"))
problem.addConstraint(c2, ("Ell", "Hen", "Oma", "Val"))
problem.addConstraint(c3, names)
problem.addConstraint(c4, names)
problem.addConstraint(c5, names)

S = problem.getSolutions()

#print(S)
print("\n".join([str(p) for p in S]))
