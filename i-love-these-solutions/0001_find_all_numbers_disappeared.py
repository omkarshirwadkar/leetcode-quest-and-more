from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(n) without extra space
        for i in range(len(nums)):
            # Getting the absolute value because we are multiplying by -1
            idx = abs(nums[i]) - 1
            # Only negating for the first time, cuz doing it even number of times will make the element positive again
            if nums[idx] > 0:
                nums[idx] *= -1
        ans = []
        for i in range(len(nums)):
            # Adding all the positive indexes
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
    
s1 = Solution()
arr = [2, 5, 6, 5, 6, 2]
print(s1.findDisappearedNumbers(arr))
