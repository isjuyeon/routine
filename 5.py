N,K=map(int,input().split())
l=[]
for _ in range(N):
    l.append(list((map(int,input().split()))))

if min(N,K)-1==0:
    print(-1)

d=True
for k in range(min(N, K), 0, -1):
    for i in range(N):
        for j in range(K):
            if (i+k<N and j+k<K) and l[i][j]==l[i+k][j]==l[i][j+k]==l[i+k][j+k]:
                print(k+1)
                d = False
                break

if d:
    print(-1)
