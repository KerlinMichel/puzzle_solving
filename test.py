from constraint import *
problem = Problem()

teas = ("a", "j", "p", "r")
temps = (190, 195, 200, 215)
prices = (4, 5, 6, 7)

def generate_domains():
    domain = []
    for t in temps:
        for p in prices:
            domain.append({"t": t, "p": p})
    return domain

domain = generate_domains()

for tea in teas:
    problem.addVariable(tea, domain)

def c1(*args):
    teas = args
    for i in range(4):
        t1 = teas[i]
        for j in range(i+1, 4):
            t2 = teas[j]
            if t1['t'] == 190 and t2['t'] == 195 and t2['p'] == t1['p'] + 1:
                return True
            if t2['t'] == 190 and t1['t'] == 195 and t1['p'] == t2['p'] + 1:
                return True
    return False


def c2(a, j, p, r):
    teas = {"a": a, "j": j, "p": p, "r": r}
    tp6 = None
    tt200 = None
    tt190 = None
    a = None 
    for i in teas:
        if i == "a":
            a = i
        if teas[i]["p"] == 6:
            tp6 = i
        if teas[i]["t"] == 200:
            tt200 = i
        if teas[i]["t"] == 190:
            tt190 = i
    #print([i for i in [a, tp6, tt200, tt190] if i != None])
    return len(set([t for t in [a, tp6, tt200, tt190] if t != None])) == 4

def c3(*args):
    #print(set([t["t"] for t in args]))
    return len(set([t["t"] for t in args])) == 4

def c4(*args):
    return len(set([t["p"] for t in args])) == 4        

problem.addConstraint(c1, teas)
problem.addConstraint(lambda p, r: p['p'] == r['p'] - 1, ("p", "r"))
problem.addConstraint(lambda p: p['t'] == 195, ("p",))
problem.addConstraint(c2, ("a", "j", "p", "r"))
problem.addConstraint(c3, ("a", "j", "p", "r"))
problem.addConstraint(c4, ("a", "j", "p", "r"))

S = problem.getSolutions()
#print(S)
print("\n".join([str(s) for s in S]))
