class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: ceil(a/b) if a/b < 0 else floor(a/b)
        }

        stack = deque()
        for idx, token in enumerate(tokens):
            if token not in ops:
                stack.append(int(token))
            else:
                # b = second_operand and a = first_operand
                b = stack.pop()
                a = stack.pop()
                val = ops[token](a, b)
                stack.append(val) # add it to the stack!
                print(a)
                print(token)
                print(b)
                print("-------------")
                print(val)
                print("#############")
        return stack[0]