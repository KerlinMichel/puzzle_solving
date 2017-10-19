from kanren import run, eq, membero, var, conde
from kanren.arith import add, gt, sub
from kanren.core import success, fail

# Ell: 0, Hen: 1, Oma: 2, Val: 3

black = var()
blue = var()
pink = var()
silver = var()

d15 = var()
d25 = var()
d35 = var()
d45 = var()

ds = [d15, d25, d35, d45]
cls = [black, blue, pink, silver]

def name_to_dist(n):
    return next((d for d in ds if d == n), None)

def c3(x):
    o = None
    for d in ds:
        if d == 2:
            o = d
    s = name_to_dist(silver)
    if o and s and ds.index(o) > ds.index(s):
        return success
    else:
        return fail

#print(c3())

cs = (eq(d35, 1), eq(silver, 1), (c3, d35))

d35S = run(1, d35, *cs)
silverS = run(1, silver, *cs)

print(d35S)
print(silverS)
