goal = [[1,2,3],[4,5,6],[7,8,0]]

def solve(p):
    while p != goal:
        for row in p:
            print(row)
        print()

        x, y = [(i, j) for i in range(3) for j in range(3) if p[i][j] == 0][0]

        if x < 2 and p[x+1][y] == goal[x][y]:
            p[x][y], p[x+1][y] = p[x+1][y], p[x][y]
        else:
            break

    print("Goal State:")
    for row in p:
        print(row)

puzzle = [[1,2,3],
          [4,5,6],
          [7,0,8]]

solve(puzzle)