def longestrepeat(s,k):
    l,left,right=[],0,1
    for left in range(len(s)):
        if k!=0:
            if s[right]!=s[left]:
                k-=1
                right += 1
            else:
                right+=1
        l.append(right-left+1)
#한 사이클을 돌고나면 left가 +1되어야 하는데 왜 짜지지가 않는거지
    print(max(l))
longestrepeat("aaabbc",k=2)
