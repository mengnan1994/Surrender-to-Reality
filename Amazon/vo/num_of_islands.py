def num_of_islands(grid):
    if not grid and not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])

    # def dfs(i, j):
    #     if grid[i][j] == '0':
    #         return
    #     grid[i][j] = '0'
    #     di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
    #     for k in range(4):
    #         ii, jj = i + di[k], j + dj[k]
    #         if 0 <= ii < m and 0 <= jj < n:
    #             dfs(ii, jj)

    import collections
    def bfs(i, j):
        q = collections.deque([(i, j)])
        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        while q:
            # print(q)
            i, j = q.popleft()
            for k in range(4):
                ii, jj = i + di[k], j + dj[k]
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                    grid[ii][jj] = '0'
                    q.append((ii, jj))

        
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                bfs(i, j)
                cnt += 1
    
    return cnt


grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
num_of_islands(grid)