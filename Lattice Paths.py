'''
Lattice paths

Show HTML problem content 
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

        1---1---1
        |   |   |
        1---2---3
        |   |   |
        1---3---6

How many such routes are there through a 20×20 grid?
So the question might look complex, but its just permutation and can be solved with combinatronics.
I'm gonna use a simple logic to solve this problem and its shown in the above diagram'''

n = 21 # grid size

grid = []

for i in range(0,n):
    temp = []
    for j in range(0,n):
        temp.append(1)
    grid.append(temp)

print(grid)
for i in range(1,n):
    for j in range(1,n):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[n-1][n-1])