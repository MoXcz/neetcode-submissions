class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                idx = len(stack)
                print(idx)
                stack.append(stack[idx - 1] + stack[idx - 2])
                continue
            if op == 'D':
                idx = len(stack)
                stack.append(2 * stack[idx - 1])
                continue
            if op == 'C':
                idx = len(stack)
                stack.pop(idx - 1)
                continue
            else:
                stack.append(int(op))
                continue
        
        score = 0
        for num in stack:
            score += num
        return score

