for i in range(3):
    N = input()
    i = 0
    res = 1
    l = []
    while i < len(N) - 1:
        if N[i] == N[i + 1]:
            res += 1
            if i == len(N) - 2:
                l.append(res)
                break
            i += 1
        else:
            l.append(res)
            res = 1
            i += 1
    print(max(l))
