def threeSumUsingTwoSum(nums):
    ansSet = set()
    n = len(nums)
    def twoSum(target, i):
        remainingSum = set()
        for j in range(n):
            if i != j:
                first = nums[j]
                second = target - nums[j]
                if second in remainingSum:
                    temp = [first, second, -target]
                    temp.sort()
                    sol = tuple(temp)
                    ansSet.add(sol)
                remainingSum.add(first)
    for i in range(n):
        twoSum(-nums[i], i)
    return list(ansSet)

def threeSumWithTwoPointers(nums):
    nums.sort()
    triplets = set()
    n = len(nums)
    for left in range(n - 2):
        mid = left + 1
        right = n - 1
        while mid < right:
            if nums[left] + nums[mid] + nums[right] == 0:
                triplets.add((nums[left], nums[mid], nums[right]))
                mid += 1
                right -= 1
            elif nums[left] + nums[mid] + nums[right] < 0:
                mid += 1
            else:
                right -= 1
    return list(triplets)