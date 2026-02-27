class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()

        bracketMap = {"(" : ")", "[" : "]", "{" : "}"}

        for char in s:
            if char in bracketMap:
                stack.append(char)
            else:
                if len(stack) < 1 or char != bracketMap[stack[-1]]:
                    return False
                stack.pop()
        
        if len(stack) > 0:
            return False
        return True

        