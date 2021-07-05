def permutation(n,k):
    result = []
    nums=[]
    for i in range(n):
        nums.append(i+1)

    def dfs(path):
        if len(path) == k and sorted(path) not in result:
            result.append(sorted(path))
            return

        for i in nums:
            if i in path:
                continue
            else:
                l = path[:]
                l.append(i)
                dfs(l)
    dfs([])

    return result

print(permutation(4,2))