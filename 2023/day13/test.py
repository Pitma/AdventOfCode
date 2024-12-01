
def check_rows(grid,one,two):
    #print("one",one,"two",two)
    if grid[one] == grid[two]:
        return True
    else:
        return False
    
def compare(row1, row2):
    differences = 0

    for char1, char2 in zip(row1, row2):
        if char1 != char2:
            differences += 1
            if differences > 1:
                break
        else:
            continue
    
    if differences == 1:
        return True
    else:
        return False 



def find_symmetry(grid,multiplier):
    rows = len(grid)
    #print("Grid",grid)
    #print("lenRoww",rows)
    found= False
    check = 0
    for i in range(rows - 1):
        #print("testing",i)
        current_row = grid[i]
        next_row = grid[i + 1]
        if current_row == next_row:
            check = i+1
            found = True
            start_row = i
            end_row = i+1
            while (start_row >= 0 and end_row <= len(grid)-1) :
                print(start_row,end_row)
                found = check_rows(grid,start_row,end_row)
                print(found)
                start_row -= 1
                end_row += 1
                if found:
                    continue
                else:
                    
                    break
                    #check = 0
            if (start_row<0 or end_row > len(grid)) and found:
                print("end reached")
                break
    if found:
        value = (check)*multiplier
        return value
    else: 
        return 0
    
    
def vertical_to_horizontal(grid):
    #transposed_grid = [row[::-1] for row in grid]
    transposed_grid = ["".join(row) for row in zip(*grid)]
    #print(transposed_grid)
    return transposed_grid

grid = []
with open("sample.txt") as sample_file:
        sample_input = sample_file.read().split('\n\n')
        grid = [line.split('\n')  for line in sample_input]
sum = 0
for index, grids in enumerate(grid):
    #print("Zeile",index)
    hor = find_symmetry(grids,100)
    #print("index",index,"horizontal",hor)
    sum += hor
    transposed_grid = vertical_to_horizontal(grids)
    vert = find_symmetry(transposed_grid,1)
    # print("index",index,"vertical",vert)
    sum += vert
    print(index, sum)
    #print("-----------")

print("Ergebnis",sum)

#print("Ergebnis",sum)
    ###39585 too high
    ###39542 too high
    #34993 correct
    ###33207 too low
    ###33250 wrong