from collections import defaultdict, deque

file = "input.txt"


Loaded_graph = defaultdict(list)

# load file and build graph from file "value"-"connects to"
def load_graph(file):
    with open(file) as f:
        for line in f:
            line = line.strip()
            value, connects_to = line.strip().split("-")
            Loaded_graph[value].append(connects_to)
            Loaded_graph[connects_to].append(value)


# for each key in paths count occurences if key is lower case
# if key is "end" return path
def count_paths(path):
    duplicates = []
    for key in path:
        if key.islower():
            if path.count(key) > 1:
                duplicates.append(key)
    if len(duplicates) > 2:
        return False
    return True


# for each key in graph go through values recursively wich are not visited yet
# if value is "end" add path to paths
# if value is lower case mark as visited
def find_all_paths(graph, start, end, visited, path=[], duplicate=False):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.get(start):
        return []
    paths = []
    if start == "start":
        visited.append(start)
    for node in graph[start]:
        if visited.count(node) < 2 and node != "start":
            # check if node is lower case
            if node.islower():
                visited.append(node)
            newpaths = find_all_paths(graph, node, end, visited, path)
            for newpath in newpaths:
                if count_paths(newpath):
                    paths.append(newpath)
            if visited[-1] == node:
                visited.pop()
    return paths


load_graph(file)
paths = find_all_paths(Loaded_graph, "start", "end", [], [], False)
t = 0
for path in paths:
    # if count_paths(path):
    # print(path)
    t += 1
print(t)

# print(len(paths))
# print(list)
# print(Loaded_graph)
