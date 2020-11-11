"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
"""


class Solution:
    def is_valid(self, string: str):
        """
        The length of string must be even, otherwise return false.

        use stack
        if current str is in ['{', '(', '['], push it in stack
        if not:
            if the str of the stack top and current str can be a valid pair, pop the stack
            if not, return false
        """
        
        if len(string) % 2 != 0:
            return False
        stack = []
        for i, s in enumerate(string):
            if len(stack) == 0:
                stack.append(s)
                continue
            if s in ['(', '[', '{']:
                stack.append(s)
            elif s == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False
            elif s == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
                else:
                    return False
            elif s == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.is_valid('[()]{}()'))

