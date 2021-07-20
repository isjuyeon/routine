import math
def binary(nums,target):
    if target not in nums:
        return -1
    a,b=0,len(nums)-1
    mid=math.floor((a+b)/2)
    while True:
        if mid<nums.index(target):
            a,mid=mid,math.floor((mid+b)/2)
        else:
            b,mid=mid,math.floor((mid+a)/2)
        if nums[mid]==target:
            if nums[mid] == target:
                return mid

print(binary([-1,0,3,5,9,12],target=2))