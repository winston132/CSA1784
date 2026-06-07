g = {0:[1,2], 1:[3], 2:[3], 3:[4], 4:[]}

path = [0]

for node in [1,3,4]:
    path.append(node)

print("Shortest path:", path)