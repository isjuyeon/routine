import heapq
def findK(nums,k):
    return heapq.nlargest(k,nums)

print(findK([3,2,3,1,2,4,5,5,6],k=4))
