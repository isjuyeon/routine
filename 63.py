def sortColors(nums):
    a, b, c = 0, 0, len(nums) - 1
    while b <= c:
        if nums[b] == 0:
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            if nums[b] == 2:
                nums[b], nums[c] = nums[c], nums[b]
                c -= 1
        elif nums[b] == 2:
            nums[b], nums[c] = nums[c], nums[b]
            c -= 1
            if nums[b] == 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
        b += 1
    return nums
print(sortColors([1,2,0,2,0,1,1,0]))
#왜 처음부터 list index밖으로 c를 설정하는거지?