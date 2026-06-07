from itertools import permutations

d = [[0,2,9,10],
     [1,0,6,4],
     [15,7,0,8],
     [6,3,12,0]]

cost = 999
best = []

for p in permutations([1,2,3]):
    tour = [0] + list(p) + [0]
    c = sum(d[tour[i]][tour[i+1]] for i in range(4))
    
    if c < cost:
        cost = c
        best = tour

print("Tour:", best)
print("Total distance:", cost)