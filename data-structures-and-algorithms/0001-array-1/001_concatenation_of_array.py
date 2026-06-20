from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    
s1 = Solution()
arr = [2, 5, 9, 10]
print(s1.getConcatenation(arr))