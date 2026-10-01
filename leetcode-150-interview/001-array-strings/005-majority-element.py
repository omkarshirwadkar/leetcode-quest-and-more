def majorityElementBySorting(nums):
    nums.sort()
    return nums[len(nums) // 2]

def majorityElementBoyerMooreVoting(nums):
    candidate = 0
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

nums = [1,1,1,1,1,4,5,2,2,2,21,1,1]
print("Majority Element in nums is: ", majorityElementBoyerMooreVoting(nums))