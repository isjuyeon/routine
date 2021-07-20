def largestNumber(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and (str(nums[j - 1])+str(nums[j])<str(nums[j])+str(nums[j-1])):
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
        i += 1
    return str(int(''.join(map(str, nums))))
print(largestNumber([3,30,34,5,9]))