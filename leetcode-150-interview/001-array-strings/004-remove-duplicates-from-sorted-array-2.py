def removeDuplicatesAtMostTwo(nums):
    ans = 1
    n = len(nums)
    isRepeat = False
    for i in range(n - 1):
        if nums[i] == nums[i + 1] and not isRepeat:
            nums[ans] = nums[i + 1]
            ans += 1
            isRepeat = True
        if nums[i] != nums[i + 1]:
            nums[ans] = nums[i + 1]
            ans += 1
            isRepeat = False
    return ans

nums = [1, 1, 1, 2, 2, 2, 4, 4, 5, 6, 7, 7, 90]
print("Before Removing Duplicates: ", *nums)
k = removeDuplicatesAtMostTwo(nums)
print("After Removing Duplicates: ", nums, k)