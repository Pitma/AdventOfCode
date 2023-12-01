import re
file = open("input_test.txt","r")
file_data = file.read()
input =  file_data.split("\n")
currentFolder = ''
sumArray = 0
folderSizes = dict()
folderRelations = []
for command in input:
    folder = re.findall('cd ([a-z]|\/)',command)
    if folder:
        if folder[0] == '/':
            folder = ['root']
        currentFolder = folder.copy()
        sumArray = 0
        print("folder",folder)
        folderSizes[currentFolder[0]] = 0
        

    if re.match('\d+',command):
        size = re.findall('\d+',command)
        print("Folder:",currentFolder[0],"size",str(size[0]))
        folderSizes[currentFolder[0]] = folderSizes[currentFolder[0]] + int(size[0])
        sumArray += int(size[0])

    if re.findall('^dir',command):
        
        folderRelations[command[0]].append(re.findall('[^dir ]+$',command))
        print("dir: ", folderRelations)
    folder.clear()

    

print(folderSizes)
print(folderRelations)
print(sumArray)    
#print(input)











