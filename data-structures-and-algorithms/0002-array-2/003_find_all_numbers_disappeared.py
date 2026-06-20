from typing import List
# Best Approach is in i-love-these-solutions folders
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_array = [True] * n
        for i in nums:
            count_array[i - 1] = False
        ans = []
        for i in range(n):
            if count_array[i]:
                ans.append(i + 1)
        return ans
    
s1 = Solution()
arr = [2, 5, 6, 5, 6, 2]
print(s1.findDisappearedNumbers(arr))
