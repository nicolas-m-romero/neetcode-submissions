class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stores pair: [temp, i]
        output = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                output[stack_i] = i - stack_i
            stack.append([temperatures[i], i])

        return output