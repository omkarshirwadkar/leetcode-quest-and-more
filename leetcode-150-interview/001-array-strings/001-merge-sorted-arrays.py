# TC: O((n + m)log(n + m))
def naiveSortAndMerge(nums1, m, nums2, n):
    for i in range(m, m + n):
        nums1[i] = nums2[i - m]
    nums1.sort()

# TC: O(n + m)
def startFromBackGreatestToSmallest(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while k >= 0:
        if i < 0:
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        elif j < 0:
            while i >= 0:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        elif nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

def threePointerCopyArray(nums1, m, nums2, n):
    # Create an array num1copy and then have 2 read pointers for num1copy and nums2 
    # and a write pointer for nums1
    return

nums2 = [2, 5, 6]
n = len(nums2)
nums1 = [1, 2, 3, 0, 0, 0]
m = len(nums1) - n
print(nums1, nums2)
startFromBackGreatestToSmallest(nums1, m, nums2, n)
naiveSortAndMerge(nums1, m, nums2, n) # Run one of them
threePointerCopyArray(nums1, m, nums2, n)
print(nums1, nums2)