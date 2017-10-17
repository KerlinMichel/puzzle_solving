from constraint import *
problem = Problem()

cars = ['cav', 'fie', 'gra', 'inj']
lps = ['fr', 'gg', 'mr', 'yg']
states = ['al', 'co', 'ha', 'lo']
fines = [25, 50, 75, 100]

def generate_domains():
    domains = []
    for l in lps:
       for s in states:
           for f in fines:
               domains.append({"l": l, "s": s, "f": f})
    return domains

domain = generate_domains()

for car in cars:
    problem.addVariable(car, domain)

def all_diff(li):
    return len(set([i for i in li if i != None])) == len(li)

def c1(*args):
    yg = None
    ha = None
    for c in args:
        if c['l'] == 'yg':
            yg = c
        if c['s'] == 'ha':
            ha = c
    return yg and ha and yg != ha and yg['f'] == ha['f'] + 25

def c2(*args):
    fr = None
    gg = None
    for i,c in enumerate(args):
        if c['l'] == 'gg':
            gg = c
        if cars[i] == 'fie':
            fr = c
    return fr and gg and fr != gg and fr['f'] < gg['f']

def c3(cav):
    return cav['s'] == 'co'

def c4(cav, fie):
    return cav['f'] == 50 or fie['f'] == 50

def c5(fie, *args):
    al = None
    for c in args:
        if c['s'] == 'al':
            al = c
    return al and al['f'] == fie['f'] + 25

def c6(gra, *args):
    fr = None
    for c in args:
        if c['l'] == 'fr':
            fr = c
    return fr and gra['f'] > fr['f']

def c7(*args):
    for c in args:
        if c['f'] == 100 and c['l'] == 'gg':
            return False
    return True

problem.addConstraint(c1, cars)
problem.addConstraint(c2, cars)
problem.addConstraint(c3, ('cav',))
problem.addConstraint(c4, ('cav', 'fie'))
problem.addConstraint(c5, ('fie', 'cav', 'gra', 'inj'))
problem.addConstraint(c6, ('gra', 'fie', 'cav', 'inj'))
problem.addConstraint(c7, cars)
problem.addConstraint(lambda *args: all_diff([c['l'] for c in args]), cars)
problem.addConstraint(lambda *args: all_diff([c['s'] for c in args]), cars)
problem.addConstraint(lambda *args: all_diff([c['f'] for c in args]), cars)

S = problem.getSolutions()

print(S)    
