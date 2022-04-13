# day 7 part 1 ---------------------------------------------------------------
from statistics import median
def getCrabSubPosList(file='data/day7CrabSubmarines.txt'):
    with open(file,'tr') as f:
        lis = [int(val) for val in f.readline().split(',')]
    return lis
subs = getCrabSubPosList()
fuel = 0
pos = int(median(subs))
for sub in subs:
    fuel += abs(sub-pos)
print(f'Overall fuel consumption: {int(fuel)}')

# day 7 part 2 ---------------------------------------------------------------
def fuelcalc(val):
    res=0
    for idx in range(1,val+1):
        res+=idx
    return res

# trial and error over a range of 100 possible optimal positions around the
# offsetted median... that's probably not the intended solution.
pos = int(median(subs))+150 
# and find correct solution via trial and error.
fuel = [0 for x in range(100)]
for sub in subs:
    for idx,p in enumerate(range(pos-50,pos+50)):
        fuel[idx] += fuelcalc(abs(sub-p))
print(f'Overall fuel consumption: {fuel[fuel.index(min(fuel))]}')