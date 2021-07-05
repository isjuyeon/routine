def permutation(nums):
    def dfs(index, path):
        if len(path) == len(nums):
            result.append([x for x in path])
            return

        for i in nums:
            if str(i) in path:
                continue
            else:
                dfs(index + 1, path + str(i))

    result = []
    dfs(0, "")

    return result

print(permutation([1,2,3]))