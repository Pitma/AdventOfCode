import hashlib
prefix = "bgvyzdsv"
number = 609043
input = prefix + str(number)

i = 0
firstFound = False
while True:
    input = prefix + str(i)
    hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    if hash[:5] == "00000" and not firstFound:
        print(hash)
        print("Found part 1: " + str(i))  # part 1
        firstFound = True
    if hash[:6] == "000000":  # part 2
        print(hash)
        print("Found part 2: " + str(i))
        break
    i += 1
