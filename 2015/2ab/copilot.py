#read file and return a list of lines and delete "\n"
def read_file(file_name):
	with open(file_name, 'r') as f:
		lines = f.readlines()
		lines = [line.rstrip('\n') for line in lines]
		return lines

files = read_file('input.txt')
print(files)