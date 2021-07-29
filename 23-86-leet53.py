def maxSubArray(nums):
    for i in range(len(nums) - 1):
        if nums[i] > 0:
            nums[i + 1] += nums[i]
    return max(nums)
print(maxSubArray([1]))
#여기서 for문의 범위가 0이니까 애초에 들어가질 않아서 예외처리 안해줘도 됨