start = (0,0)
goal = (4,4)

path = []

for x in range(5):
    path.append((x,0))

for y in range(1,5):
    path.append((4,y))

print("Path:", path)