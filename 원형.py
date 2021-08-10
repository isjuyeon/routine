n,k=map(str,input().split())
res=0
K='1'+k
for i in range(len(K)-1):
	res+=min(abs(int(K[i+1])-int(K[i])),int(n)-abs(int(K[i+1])-int(K[i])))
print(res)