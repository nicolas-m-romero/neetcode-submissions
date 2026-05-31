class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        stack = []

        for bracket in s:
            if bracket in pairs and stack and stack[-1] == pairs[bracket]:
                stack.pop()
            else:
                stack.append(bracket)

        return len(stack) == 0