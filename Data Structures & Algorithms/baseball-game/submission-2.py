class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                idx = len(stack)
                stack.append(stack[idx - 1] + stack[idx - 2])
            elif op == 'D':
                idx = len(stack)
                stack.append(2 * stack[idx - 1])
            elif op == 'C':
                idx = len(stack)
                stack.pop(idx - 1)
            else:
                stack.append(int(op))
        
        return sum(stack)

