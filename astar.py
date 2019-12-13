# Using A-star searching to solve tha snake game
# For the snake game, the basic rule is to lead a little snake to find and a apple.
# It can be treated as a game to find a path from a current position to other position.
# The snake can has four opions up, down, left and right. The snake is moving following the current direction continuely.
# It cannot turn around without any moving space. That means it terminates the game if choosing the opposite direction.
# That means the snake has three options in each step.
#   Stay at current direction
#   turn a direction which is a perpendicular with the current direction.
#
# Using manhattan distance between a snake head and the apple as h, 
# In the regular case, it should equal to the h_true. but when meeting itself body or other case,
# a snake need a detour, which proves its is admissiable.

import numpy as np 
import collections


def aStarSearching(snake_x,snake_y, apple_x,apple_y,step,direction):
    snake = [(snake_x[i], snake_y[i]) for i in range(len(snake_x))]
    fronter = collections.defaultdict(int)
    fronter[snake[0]] = GetH(snake[0][0],snake[0][1],apple_x,apple_y)
    exploied = []
    count = 0
    while len(fronter)!= 0:
        print("Fronter: ", fronter, "\n")
        position, h = sorted(fronter.items(), key=lambda t: t[1])[0]
        fronter.pop(position)
        print("pop Fronter: ", position ," h: ", h,"\n")
        # Explored the frintier and  add to explored if not there
        if position not in exploied: exploied.append(position)
        # reach the target return the direction
        if position[0]== apple_x and position[1] == apple_y:
            if count == 0: return direction
            return translateSign(exploied[1][0],exploied[1][1], exploied[0][0], exploied[0][1])

        
        for i in ["x","y"]:
            for j in [-1,1]:
                if i == "x":
                    xnew = position[0]+j*step
                    ynew = position[1]
                if i == "y":
                    ynew = position[1] + j*step
                    xnew = position[0]
                if (xnew, ynew) in snake: continue
                if (xnew < 0 or ynew < 0): continue
                if (xnew, ynew) in fronter.keys():
                    fronter[(xnew,ynew)] = min(fronter[(xnew,ynew)], GetH(xnew,ynew,apple_x,apple_y)+count)
                else:
                    fronter[(xnew,ynew)] = GetH(xnew,ynew,apple_x,apple_y) + count
        print("After exploring Current explied:", exploied, "\n")
        count += 1
        if count > 3: break
    print("After exploring Current explied:", exploied, "\n")
    if len(exploied)<2: return direction
    return translateSign(exploied[1][0],exploied[1][1], exploied[0][0], exploied[0][1])

    

def GetH (x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def translateSign(x1,y1,hx,hy):
    if x1>hx: 
        print("Selected Right")
        return 1
    if x1<hx:
        print("Selected Left") 
        return 2
    if y1>hy: 
        print("Selected Down")
        return 4
    if y1<hy: 
        print("Selected Up")
        return 3
