from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }


        stack = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue
            if c == ')' or c == ']' or c == '}':
                if len(stack) == 0:
                    return False
                if pairs[stack.pop()] != c:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False