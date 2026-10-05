def isSubsequence(s,t):
    ptr1 = ptr2 = 0
    n, m = len(s), len(t)
    while ptr2 < m and ptr1 < n:
        if s[ptr1] == t[ptr2]:
            ptr1 += 1
        ptr2 += 1
    return ptr1 == n

s = "str"
t = "satire"
print("Is s a subsequence of t: ", isSubsequence(s, t))