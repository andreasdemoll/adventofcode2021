# day10 part 1 ---------------------------------------------------------------
# make a stack with the opened bracket types. Push when opening, pop when
# closing. If a pop of wrong type occurs, line is corrupt.
# if at line end, the stack is not empty, the line is incomplete.

types = {')':'(',']':'[','>':'<','}':'{'}
code  = {')':3, ']':57, '}':1197, '>':25137}


def checkline(line):
    points = 0
    stack=[]
    for c in line:
        if c in types.values(): stack.append(c)
        elif c in types.keys():
            if stack[-1] != types[c]:
                #print(f'error for {c}')
                points = code[c]
                break
            else:
                stack.pop(-1)
    return points

with open('data/day10NavigationSubsys.txt','rt') as f:
    p=0
    for line in f:
        p+=checkline(line)
    print(f'points: {p}')
    
# day10 part 2 ---------------------------------------------------------------
def checkline2(line):
    stack=[]
    for c in line:
        if c in types.values(): stack.append(c)
        elif c in types.keys():
            if stack[-1] != types[c]: #corrupt line
                return -1
            else:
                stack.pop(-1)
    return stack


def calcScore(t):
    scores = {')':1,']':2,'}':3,'>':4}
    sc=0
    for ele in t:
        sc*=5
        sc += scores[ele]
    return sc

typesR= {'(':')','[':']','<':'>','{':'}'}
total_scores = []
with open('NavigationSubsys.txt','rt') as f:
    for line in f:
        res = checkline2(line)
        if res != -1:
            t = [typesR[x] for x in checkline2(line)]
            t.reverse()
            sc = calcScore(t)
            total_scores.append(sc)
            add = ''.join(t)
            #print(f'added: {add}, score: {sc}')
            
total_scores.sort()
print(f'middle score: {total_scores[round(len(total_scores)/2)]}')