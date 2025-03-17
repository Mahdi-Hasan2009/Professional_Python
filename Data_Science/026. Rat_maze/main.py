def valid__path(maze, i, j, m, n):
  if i == m or j == n:
    return False
  if maze[i][j] == 1:
    return False
  return True

def rat_maze(maze, i, j, m, n , arr):
  if arr[-1][-1] == 1:
    return True
  if valid__path(maze, i, j, m, n):
    arr[i][j] =  1
    if rat_maze(maze, i + 1, j, m, n, arr):
      return True
    if rat_maze(maze, i, j+1, m, n , arr):
      return True
    arr[i][j] = 0
    return False
  
maze = [[0, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 1, 0]]

arr = [[0 for i in range(len(maze[0]))] for j in range(len(maze))]
rat_maze(maze, 0, 0, len(maze), len(maze[0]), arr)
for i in arr:
  print(i)