from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hundred_sized_array = [0] * 101
        for i in nums:
            hundred_sized_array[i] += 1
        ans = []
        for i in nums:
            ans.append(sum(hundred_sized_array[:i]))
        return ans
       
s1 = Solution()
arr = [2, 5, 9, 10, 12, 11, 2, 1, 3, 3, 3, 5]
print(s1.smallerNumbersThanCurrent(arr))