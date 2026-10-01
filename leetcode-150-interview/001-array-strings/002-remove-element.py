def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

nums = [1, 2, 3, 2, 2, 5, 19, 3, 3]
val = [2]
print("Mismatched elements: ", removeElement(nums, val))