i=0
l=[0]
def recursion(s):
    k=0
    global i
    while i<len(s)-1:
        if s[i]==s[i+1]:
            k+=1
            i+=1
        else:
            if k==0:
                l.append(k)
            else:
                l[-1]+=k
            recursion(s[i+1:])
            break
            #똑같은 일을 하지 말라는 의미에서 break를 걸어준다.
print(recursion('110225644448888'))
