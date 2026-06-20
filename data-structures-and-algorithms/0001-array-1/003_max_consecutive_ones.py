from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currOnes = 0
        maxOnes = 0
        for i in nums:
            if i:
                currOnes += 1
            else:
                currOnes = 0
            maxOnes = max(maxOnes, currOnes)
        return maxOnes
    
s1 = Solution()
arr = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]
print(s1.findMaxConsecutiveOnes(arr))