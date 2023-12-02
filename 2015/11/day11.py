import re
import numpy as np

isTest = False

if isTest:
    file = open("sample.txt","r")
else:
    file = open("input.txt","r")

file_data = file.read().split("\n")

games = []
for line in file_data:
    games.append(line.split(":")[1])

testResult1 = 8
testResult2 = 2286

colors = ["red","green", "blue"]
max = [12,13,14]

def solvePartI(): 
    cnt = 1
    sum = 0
    for game in games:
        isGood=True
        for color in colors:
            pulls = re.findall("[0-9]+."+color,game)
            colorsMax = 0
            for pull in pulls:
                amount=re.findall("\d+",pull)
                if(max[colors.index(color)] < int(amount[0])):
                    #print("Leider zu Hoch im Game",cnt,"Pull",pull,"Max Wert",max[colors.index(color)])
                    isGood =False
                    break 
        if isGood:
            sum +=cnt
        cnt+=1

    if isTest:
        if sum == testResult1:
            print("Result Part I",sum)
        else: 
            print("ERROR Part I is not correct")
    else:
        print("Result Part I",sum)

def solvePartII(): 
    cnt = 0
    sum = 0
    gameResults = []
    
    for game in games:
        colorMaxArray = [0,0,0]
        for color in colors:
            pulls = re.findall("[0-9]+."+color,game)
            colorsMax = 0
            for pull in pulls:
                amount=re.findall("\d+",pull)
                if(int(amount[0]) > colorsMax):
                    colorsMax = int(amount[0])
                # if(max[colors.index(color)] < int(amount[0])):
                #     #print("Leider zu Hoch im Game",cnt,"Pull",pull,"Max Wert",max[colors.index(color)])
                #     isGood =False
                #     break 
            colorMaxArray[colors.index(color)] += colorsMax
        
        cnt+=1
        gameResults.append(np.prod(colorMaxArray))

    if isTest:
        if np.sum(gameResults) == testResult2:
            print("Result part II",np.sum(gameResults))
        else: 
            print("ERROR Part II is not correct")
    else:
        print("Result part II",np.sum(gameResults))

solvePartI()
solvePartII()




