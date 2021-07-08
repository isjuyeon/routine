def numset(nums):
    result=[]
    def dfs(path):
        if (path != None) and sorted(path) not in result:
            result.append(path)
        for i in nums:
            if i not in path:
                l=path[:]
                l.append(i)
                dfs(l)
    dfs([])
    return result

print(numset([1,2,3]))
dp