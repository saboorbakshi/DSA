class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char.lower()
        
        n = len(newS)
        for i in range(n):
            j = n - i - 1
            if i != j and newS[i] != newS[j]:
                return False
        
        return True
        

        