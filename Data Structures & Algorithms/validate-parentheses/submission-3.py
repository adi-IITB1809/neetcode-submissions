class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        Compli = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i in s:

            if i == '(' or i == '[' or i == '{':
                stack.append(i)

            else:
                if stack and Compli[stack[-1]] == i:
                    stack.pop()
                else:
                    return False

        return not stack