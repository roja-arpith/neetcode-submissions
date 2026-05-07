class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i not in "+DC":
                stack.append(int(i))
            elif i == "+":
                num2 = stack.pop()
                num1 = stack.pop()

                res = num1 + num2
                stack.append(num1)
                stack.append(num2)
                stack.append(res)
            elif i == "D":
                num = stack.pop()

                res = num * 2

                stack.append(num)
                stack.append(res)
            elif i == "C":
                stack.pop()
        
        return sum(stack)

