n,truckSize=input().split()
truckSize=int(truckSize)
l=[]
for i in range(int(n)):
    l.append(list(map(int,input().split())))
a=sorted(l,key=lambda x:-x[1])

result=0
i=0
while truckSize>0:
    if truckSize>=int(a[i][0]):
        result+=int(a[i][0])*int(a[i][1])
        truckSize -= int(a[i][0])
    else:
        result+=truckSize*int(a[i][1])
        truckSize =0
    i+=1
print(int(result))