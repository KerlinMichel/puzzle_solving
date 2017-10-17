from constraint import *
problem = Problem()

captains = ["arm", "jac", "rom", "yan"]
boats = ["dr", "fr", "sa", "wp"]
locs = ["as", "bb", "rr", "tt"]
manatees = [3, 4, 5, 6]

def generate_domains():
    domains = []
    for b in boats:
        for l in locs:
            for m in manatees:
                domains.append({"b": b, "l": l, "m": m})
    return domains

domain = generate_domains()

def all_diff(li):
    return len(set([i for i in li if i != None])) == len(li)

for cap in captains:
    problem.addVariable(cap, domain)

def c1(*args):
    for i, c in enumerate(args):
        if c['b'] == 'dr':
            if (c['l'] == 'rr') ^ (captains[i] == 'rom'):
                return True
    return False

def c2(*args):
    rr = None
    wp = None
    for c in args:
        if c['l'] == 'rr':
            rr = c
        if c['b'] == 'wp':
            wp = c
    return rr and wp and rr['m'] < wp['m']
        
def c3(yang, arm, jac, rom):
    caps = {"arm": arm, "jac": jac, "rom": rom}
    rr = None
    sa = None
    for c in caps:
        if caps[c]['l'] == 'rr':
            rr = c
        if caps[c]['b'] == 'sa':
            sa = c
    return all_diff(["yan", rr, sa])

def c4(*args):
    bb = None
    rr = None
    for c in args:
        if c['l'] == 'rr':
            rr = c
        if c['l'] == 'bb':
            bb = c
    return bb and rr and bb['m'] == rr['m'] + 2

def c5(*args):
    for c in args:
        if c['m'] == 5 and c['l'] == 'as':
            return False
    return True

def c6(*args):
    for i, c in enumerate(args):
        if c['m'] == 3:
            if (captains[i] == 'yan') ^ (c['b'] == 'sa'):
               return True
    return False

def c7(*args):
    fr = None
    bb = None
    fr_c = None
    bb_c = None
    for i, c in enumerate(args):
        if c['b'] == 'fr':
            fr = c
            fr_c = captains[i]
        if c['l'] == 'bb':
            bb = c 
            bb_c = captains[i]
    return fr and bb and ((fr['m'] == 3 and bb_c == 'arm') or (fr_c == 'arm' and bb['m'] == 3))

def c8(*args):
    for c in args:
        if c['b'] == 'sa' and c['l'] != 'bb':
            return False
    return True

problem.addConstraint(c1, captains)
problem.addConstraint(c2, captains)
problem.addConstraint(c3, ("yan", "arm", "jac", "rom"))
problem.addConstraint(c4, captains)
problem.addConstraint(c5, captains)
problem.addConstraint(c6, captains)
problem.addConstraint(c7, captains)
problem.addConstraint(c8, captains)
problem.addConstraint(lambda *args: all_diff([c["b"] for c in args]), captains)
problem.addConstraint(lambda *args: all_diff([c["l"] for c in args]), captains)
problem.addConstraint(lambda *args: all_diff([c["m"] for c in args]), captains)

S = problem.getSolutions()

print(S)
#print("\n".join([str(s) for s in S][:5]))
