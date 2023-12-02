import re
import numpy as np

isTest = False

if isTest:
    password = 'abcdefgh'
else:
    #password = 'hxbxwxba' #part1
    password = 'hxbxxyzz' #part2
testResult1 = 'abcdffaa'
isValid = False

def generiere_array():
    alle_kleinbuchstaben = [chr(ord('a') + i) for i in range(26)]
    no_i_l = [buchstabe for buchstabe in alle_kleinbuchstaben]# if buchstabe not in ('i', 'l','o')]

    return no_i_l

validLetters = generiere_array()

def nextPassword(oldPassword):
    
    done = False
    oldList = [*oldPassword]
    pwLength = len(oldList)
    currPos = 1
    
    for i in range(0,len(oldList)-1):
         if oldList[i] in ('i','l','o'):
             oldList[i] = chr(ord(oldList[i])+1)
             for a in range(i+1,len(oldList)-1):
                 oldList[a] = 'a'
             break

    while not done:
        pos = pwLength - currPos
        if(oldList[pos] == 'z'):
            oldList[pos] = 'a'
            currPos+=1
        else:
            oldList[pos] = validLetters[validLetters.index(oldList[pos])+1]
            done = True
    
    return ''.join(oldList)

def validatePassword(password):
    isValid = False
    
    cnt = 0
    for i in range(0,len(password)-3):
        if(ord(password[i])+1 == ord(password[i+1])):
           #print("passed 1")
           if(ord(password[i+1])+1 == ord(password[i+2])):
               #print("passed 2") 
               cnt += 1
               #print("Valid abc")
               break
    found = []
    for i in range(0,len(password)-1):
         if(ord(password[i]) == ord(password[i+1]) and password[i] not in found):
             cnt += 1
             #print("Valid bb", cnt)
             found.append(password[i])
    # print(password[i],password[i+1])
    # print(found)
    # print(password)
    # print(cnt)
    # if password == 'ghjaabcc':
    #     isValid = True
    if(cnt>2 and len(found) > 1):
        isValid = True
    #print(isValid)

    return isValid  

    


def solvePartI(): 
    valid = False
    newPassword = password
    while not valid:
        newPassword = nextPassword(newPassword)
        valid = validatePassword(newPassword)
    
    print("Ergebnis", newPassword)
        

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





