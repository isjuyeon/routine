def comsum(candidates,target):
    result=[]
    def dfs(path):
        if sum(path)==target and path not in result:
            result.append(path)
        elif sum(path)>target:
            result.append()
        for i in candidates:
            l=path[:]
            l.append(i)
            dfs(l)
    dfs([])
    return result