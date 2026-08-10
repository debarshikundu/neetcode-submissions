class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        for i in range(len(s)):
            newStr = ""
            newStr = s[0:i]+s[i+1:]
            if self.isValid(newStr):
                return True
        return False

    def isValid(self, s: str) -> bool:
        return s==s[::-1]
            
