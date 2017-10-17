from constraint import *
problem = Problem()

drugs = ['biz', 'dam', 'fav', 'gra']
conds = ['df', 'di', 'hd', 'in']
srcs = ['be', 'br', 'fr', 'mu']
months = [1, 2, 3, 4]

def generate_domains():
    domains = []
    for c in conds:
       for s in srcs:
           for m in months:
               domains.append({"c": c, "s": s, "m": m})
    return domains

domain = generate_domains()

for drug in drugs:
    problem.addVariable(drug, domain)

def all_diff(li):
    return len(set([i for i in li if i != None])) == len(li)

def c1(*args):
   mu = None
   for d in args:
      if d['s'] == 'mu':
          mu = d
   return mu and mu['c'] == 'hd'

def c2(*args):
   be = None
   for d in args:
      if d['s'] == 'be':
          be = d
   return be and be['c'] == 'df'

def c3(*args):
    hd = None
    hd_d = None 
    be = None
    be_d = None
    for i,d in enumerate(args):
        if d['c'] == 'hd':
            hd = d
            hd_d = drugs[i]
        if d['s'] == 'be':
            be = d
            be_d = drugs[i]
    return hd and be and ((hd_d == 'dam' and be['m'] == 3) ^ (hd['m'] == 3 and be_d == 'dam'))

def c4(fav, *args):
    di = None
    for d in args:
        if d['c'] == 'di':
            di = d
    return di and fav['m'] == di['m'] + 2

def c5(*args):
    ap = None
    di = None
    br = None
    for i,d in enumerate(args):
        if d['m'] == 4:
            ap = drugs[i]
        if d['c'] == 'di':
            di = drugs[i]
        if d['s'] == 'br':
            br = drugs[i]
    return all_diff([ap, di, br])

def c6(gra):
    return (gra['m'] == 3) ^ (gra['s'] == 'br')

problem.addConstraint(c1, drugs)
problem.addConstraint(c2, drugs)
problem.addConstraint(c3, drugs)
problem.addConstraint(c4, ('fav', 'biz', 'dam', 'gra'))
problem.addConstraint(c5, drugs)
problem.addConstraint(c6, ('gra',))
problem.addConstraint(lambda f: f['s'] != 'be', ('fav',))

problem.addConstraint(lambda *args: all_diff([d["c"] for d in args]), drugs)
problem.addConstraint(lambda *args: all_diff([d["s"] for d in args]), drugs)
problem.addConstraint(lambda *args: all_diff([d["m"] for d in args]), drugs)

S = problem.getSolutions()

print(S)
