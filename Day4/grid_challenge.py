def gridChallenge(grid):
    res = collections.defaultdict(list)
    
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            res[j].append(grid[i][j])
    
    for row in res.values():
        if row != sorted(row):
            return 'NO'
    return 'YES'