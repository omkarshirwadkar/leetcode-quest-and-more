from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = ((n + 1) * n) // 2
        unique_sum = sum(list(set(nums)))
        array_sum = sum(nums)
        return [array_sum - unique_sum, actual_sum - unique_sum]
    
s1 = Solution()
arr = [2, 5, 1, 4, 4]
print(s1.findErrorNums(arr))
