/**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
 */
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                if nums[a]+nums[b] == target:
                    return [a,b]
