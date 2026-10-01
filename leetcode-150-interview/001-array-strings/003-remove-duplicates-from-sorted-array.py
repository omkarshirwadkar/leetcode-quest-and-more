def removeDuplicates(nums):
    ans = 1
    n = len(nums)
    for i in range(n - 1):
        if nums[i] != nums[i + 1]:
            nums[ans] = nums[i + 1]
            ans += 1
    return ans

nums = [1, 1, 1, 2, 2, 2, 4, 4, 5, 6, 7, 7, 90]
print("Before Removing Duplicates: ", *nums)
k = removeDuplicates(nums)
print("After Removing Duplicates: ", nums, k)