cycles = 80
# read inputTest.txt and return array of values split by comma
def readFile():
    with open("input.txt", "r") as f:
        return f.read().split(",")


startFishs = readFile()

# print("Start: " + str(startFishs))

# create fish class with age and ready
class Fish:
    def __init__(self, age):
        # print("Fish created")
        self.age = age
        self.ready = False

    # method to age fish by reducing age by 1
    # if age is below 0 , set age to 6 and add a new fish to the array with age 8
    def ageFish(self):
        # if self.ready == True:
        self.age = self.age - 1
        if self.age >= 0:
            return self.age
        else:
            # print("New Fish")
            self.age = 6
            fishs.append(Fish(8))

        self.ready = True


# for startFishs create fish array with Fish objects
fishs = []
for i in range(len(startFishs)):
    fishs.append(Fish(int(startFishs[i])))

for i in range(cycles):
    # print("Cycle: " + str(i))
    # for cycles go through all fishs and update their age
    for k in range(len(fishs)):
        fishs[k].ageFish()

print(len(fishs))
