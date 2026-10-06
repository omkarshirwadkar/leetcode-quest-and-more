def maxArea(height):
    ans = 0
    left, right = 0, len(height) - 1
    while left < right:
        ans = max(ans, (right - left) * min(height[left], height[right]))
        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1
    return ans
nums = [10, 20, 15, 2, 9, 8, 7]
print("The Most Water nums can hold is: ", maxArea(nums))