inputs = []
with open('input.txt') as f:
    inputs = f.readlines()

# check if inputstring contains at least three vowels


def check_vowels(inputstring):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in inputstring:
        if char in vowels:
            count += 1
    if count >= 3:
        return True
    else:
        return False

# check if inputstring contains at least one letter that appears twice in a row


def check_double(inputstring):
    for i in range(len(inputstring)-1):
        if inputstring[i] == inputstring[i+1]:
            return True
    return False

# check if inputstring not contains the strings ab, cd, pq, or xy


def check_forbidden(inputstring):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for string in forbidden:
        if string in inputstring:
            return False
    return True


# check all inputstrings and count the number of nice strings
nice_strings = 0
for inputstring in inputs:
    if check_vowels(inputstring) and check_double(inputstring) and check_forbidden(inputstring):
        nice_strings += 1

print(nice_strings)
