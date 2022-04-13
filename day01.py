with open('data/day1depths.txt') as f:
    depths = [int(val.strip()) for val in f.readlines()]

# day 1 part 1 ---------------------------------------------------------------
def countInc(vec):
    increasedCtr = 0;
    for d0, d1 in zip(vec[:-1],vec[1:]):
        increasedCtr += (d1-d0) > 0
    return increasedCtr
print(f'{countInc(depths)} depths are deeper than previous depth.')

# day 1 part 2 ---------------------------------------------------------------
su=[]
for idx in range(len(depths)-2):
    su.append(sum(depths[idx:idx+3]))
print(f'{countInc(su)} windowed depths are deeper than previous depth.')
