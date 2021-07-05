def permutation(nums,target):
    result = []
    def dfs(path):
        if sum(path) == target and sorted(path) not in result:
            result.append(path)
            return
        elif sum(path)>target:
            return

        for i in nums:
            l=path[:]
            l.append(i)
            dfs(l)
    dfs([])

    return result

print(permutation([2,3,5],8))