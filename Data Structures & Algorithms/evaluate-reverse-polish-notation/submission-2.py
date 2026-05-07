class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        sign_stack = []

        res = 0

        for i in tokens:
            if i not in "+-*/":
                num_stack.append(int(i))
            elif i == "+":
                num1 = num_stack.pop()
                num2 = num_stack.pop()

                res = num2 + num1
                num_stack.append(res)
            elif i == "*" :
                num1 = num_stack.pop()
                num2 = num_stack.pop()

                res = num2 * num1
                num_stack.append(res)
            elif i == "-":
                num1 = num_stack.pop()
                num2 = num_stack.pop()

                res = num2 - num1
                num_stack.append(res)
            elif i == "/":
                num1 = num_stack.pop()
                num2 = num_stack.pop()

                res = int(num2 / num1)
                num_stack.append(res)
        
        return num_stack[-1]
