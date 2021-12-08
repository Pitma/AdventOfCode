santasCurrentLocation = [0, 0]
roboSantaCurrentLocation = [0, 0]
santasVisitedHouses = []
santasRoute = []
roboSantaRoute = []

# import input and generate array split each character
with open('input.txt', 'r') as f:
    input = f.read()
    santasRoute = input[::2]
    roboSantaRoute = input[1::2]
    print(santasRoute)
    print(roboSantaRoute)

# for each character as command in santasRoute create modify santastart and add to santastart if the vector is not in santastart
# if the current location is not in santasVisitedHouses add it to santasVisitedHouses
for char in santasRoute:
    if char == '>':
        santasCurrentLocation[0] += 1
    elif char == '<':
        santasCurrentLocation[0] -= 1
    elif char == '^':
        santasCurrentLocation[1] += 1
    elif char == 'v':
        santasCurrentLocation[1] -= 1
    if santasCurrentLocation not in santasVisitedHouses:
        # santasVisitedHouses.append(santasCurrentLocation)
        santasVisitedHouses.append(santasCurrentLocation[:])

for char in roboSantaRoute:
    if char == '>':
        roboSantaCurrentLocation[0] += 1
    elif char == '<':
        roboSantaCurrentLocation[0] -= 1
    elif char == '^':
        roboSantaCurrentLocation[1] += 1
    elif char == 'v':
        roboSantaCurrentLocation[1] -= 1
    if roboSantaCurrentLocation not in santasVisitedHouses:
        # santasVisitedHouses.append(santasCurrentLocation)
        santasVisitedHouses.append(roboSantaCurrentLocation[:])

print(len(santasVisitedHouses))
