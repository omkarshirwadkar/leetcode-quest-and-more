def twoSumWithArraySorted(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
        elif numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
    return [-1, -1]

nums = [1, 2, 3, 6, 21, 44]
target = 50
print("Indices for the target sum: ", twoSumWithArraySorted(nums, target))