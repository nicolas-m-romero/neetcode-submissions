class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = len(temperatures)*[0]

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                days = stack.pop()
                output[days] = i - days

            stack.append(i)

        return output
            