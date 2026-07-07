class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {"}":"{", ")":"(", "]": "["}
        stack = []
        for p in s:
            if p in close_to_open:
                if stack != [] and stack[-1] == close_to_open[p]:
                    stack = stack[:-1]
                else:
                    return False
            else:
                stack.append(p)
        return stack == []

        