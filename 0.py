def permute(nums):
    result = []

    def dfs(path):
        if len(path) == len(nums) and path not in result:
            result.append(path)
            return
        for i in nums:
            if i not in path:
                l = path[:]
                l.append(i)
                dfs(l)

    dfs([])
    if not nums:
        return False
    return result

nums = list(map(int, input().split()))

print(permute(nums))