from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans

s1 = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(s1.shuffle(arr, 4))