class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == ')' or c == ']' or c == '}':
                peek = stack[-1] if len(stack) > 0 else ''
                if c == ')' and peek == '(':
                    stack.pop()
                    continue
                if c == '}' and peek == '{':
                    stack.pop()
                    continue
                if c == ']' and peek == '[':
                    stack.pop()
                    continue
                stack.append(c)
            elif c == '(' or c == '{' or c == '[':
                stack.append(c)
        print(f"Final stack {stack}")
        return len(stack) == 0
        