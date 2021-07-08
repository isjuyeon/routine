def islands(grid):
    def dfs(i,j):
        if i<0 or i>len(grid) or j<0 or j>len(grid[0]):
            return
        grid[i][j]==0
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    count=0
    for i in range(grid):
        for j in range(grid[0]):
            dfs(i,j)
            count+=1
    return count
