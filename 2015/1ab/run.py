# read inputTest.txt and return array of values split by comma
def readFile():
    with open("input.txt", "r") as f:
        return f.read()

#count occurances of "(", ")", and increase count by 1 if "(" is found
#decrease count by 1 if ")" is found
#return position where count is 0
def findBalanced(string):
	count = 1
	for i in range(len(string)):
		if string[i] == "(":
			count += 1
		elif string[i] == ")":
			count -= 1
		if count == 0:
			return i
	return -1

print(readFile().count("(")-readFile().count(")")) #part 1
print(findBalanced(readFile())+1) #part 2