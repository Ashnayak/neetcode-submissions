class Solution:
    def isPalindrome(self, s: str) -> bool:
        D = ""
        for c in s:
            if c.isalnum():
                D += c.lower()
        return D == D[::-1]