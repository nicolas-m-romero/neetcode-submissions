class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        starts = set()

        # iterate through array and find starts of sequence
        for value in nums:
            if value - 1 not in n: # identify the start of sequence
                starts.add(value)

        # iterate through all numbers
        # build length using starts
        output = 0
        for s in starts:
            length = 1
            next_val = s + 1
            while next_val in n:
                length += 1 
                next_val += 1
            output = max(length, output)

        return output