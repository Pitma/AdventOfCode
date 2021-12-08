import itertools
inputs = []
# read inputs (startlocation, destination, distance) from file split by "to" and "=" and remove "\n"
with open('input.txt', 'r') as f:
    for line in f:
        inputs.append([line.split("to")[0], line.split(
            "to")[1].split("=")[0], line.split("=")[1]])

# remove "\n" from all inputs
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        inputs[i][j] = inputs[i][j].replace("\n", "").replace(" ", "")

# create list of all unique cities from inputs
cities = []
for i in range(len(inputs)):
    if inputs[i][0] not in cities:
        cities.append(inputs[i][0])
    if inputs[i][1] not in cities:
        cities.append(inputs[i][1])


# create list of all possible mutations of cities in one combination
mutations = list(itertools.permutations(cities, len(cities)))

# find each distance between cities in mutations and add distance to list to mutate
distances = []
for mutation in mutations:
    distance = 0
    for i in range(len(mutation)-1):
        for j in range(len(inputs)):
            if mutation[i] == inputs[j][0] and mutation[i+1] == inputs[j][1]:
                distance += int(inputs[j][2])
            elif mutation[i] == inputs[j][1] and mutation[i+1] == inputs[j][0]:
                distance += int(inputs[j][2])

    distances.append(distance)


print(min(distances))  # part 1
print(max(distances))  # part 2
