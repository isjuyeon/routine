def letterCombinations(n,k):
    digits=[]
    for i in range(1,n+1):
        digits.append(i)

    def dfs(path):
        # 끝까지 탐색하면 백트래킹
        if len(path) == k:
            if sorted(path) not in result:
                result.append(path)
            return

        # 입력값 자릿수 단위 반복
        for i in digits:
            if i not in path:
                l=path[:]
                l.append(i)
                dfs(l)

    # 예외 처리
    if not digits:
        return []

    result = []
    dfs([])

    return result
print(letterCombinations(4,2))