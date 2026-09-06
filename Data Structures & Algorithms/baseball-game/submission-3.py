class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0

        for op in operations:
            if op == '+':
                idx = len(stack)
                stack.append(stack[idx - 1] + stack[idx - 2])
                result += stack[idx - 1] + stack[idx - 2]
            elif op == 'D':
                idx = len(stack)
                stack.append(2 * stack[idx - 1])
                result += 2 * stack[idx - 1]
            elif op == 'C':
                idx = len(stack)
                result -= stack.pop(idx - 1)
            else:
                stack.append(int(op))
                result += int(op)
        
        return result

