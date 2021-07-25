class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        for(i in 0 until nums.size -1) if(target-nums[i] in nums) {
            return nums.find{ it == target-nums[i] }?.let { intArrayOf(i, it) }!!
        }
        return intArrayOf()//빈리스트를 반환함.
    }
}
