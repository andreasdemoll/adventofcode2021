# day 2 part 1 ---------------------------------------------------------------
import csv

def calcPos(commands):
    comsCodes = {'up':[0,-1], 'down':[0,1], 'forward':[1,0]} #[x,y]
    x,y = 0,0
    for row in commands:
        dx,dy = [cmd * int(row[1]) for cmd in comsCodes[row[0]]]
        x+=dx
        y+=dy
    return x,y

def openCmdsAndPrintPos(file='data/day2ControlCommands.csv', fun=calcPos):
    with open(file, newline='') as csvfile:
        commands = csv.reader(csvfile, delimiter=' ')
        x,y = fun(commands)
        print(f'we are at position {x} and depth {y}. '
              f'Position * depth = {x*y}')

openCmdsAndPrintPos()

# day 2 part 2 ---------------------------------------------------------------
def calcPosNew(commands):
    comsCodes = {'up':[1,0], 'down':[-1,0], 'forward':[0,1]} #[aim,x]
    x,y,aim = 0,0,0
    for row in commands:
        da, dx = [cmd * int(row[1]) for cmd in comsCodes[row[0]]]
        aim+=da
        x+=dx
        if dx>0:
            y -= aim * dx
    return x,y

openCmdsAndPrintPos(fun=calcPosNew)