class MinStack(object):

    def __init__(self):
        self.min = deque()
        self.stack = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # if len(self.min) < 1:
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1], val))
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()