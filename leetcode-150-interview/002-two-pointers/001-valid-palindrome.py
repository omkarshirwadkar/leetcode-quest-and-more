def isPalindromeMoreLines(s):
    def isAlphaNumeric(s):
        return s.isalnum()
    def isCapital(s):
        return ord("A") <= ord(s) <= ord("Z")
    modifiedString = []
    for i in range(len(s)):
        curr = s[i]
        if isAlphaNumeric(curr):
            if isCapital(curr):
                curr = chr(ord(curr) + 32)
            modifiedString.append(curr)
    ans = True
    i = 0
    j = len(modifiedString) - 1
    while i <= j:
        if modifiedString[i] != modifiedString[j]:
            ans = False
            break
        i += 1
        j -= 1
    return ans

def isPalindromeSmallCode(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True

s1 = "consistency beats what? talent"
s2 = "alarmrala"
print("Is S1 a palindrome: ", isPalindromeSmallCode(s1))
print("Is S2 a palindrome: ", isPalindromeSmallCode(s2))