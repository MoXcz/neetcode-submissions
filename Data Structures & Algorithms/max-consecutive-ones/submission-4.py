class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0
        for num in nums:
            count = count + 1 if num else 0
            maxCount = max(maxCount, count)
        
        return maxCount