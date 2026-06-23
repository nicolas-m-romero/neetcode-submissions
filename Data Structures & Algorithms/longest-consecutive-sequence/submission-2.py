class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums) # unique numbers within nums
        longest = 0

        for value in n:
            if value - 1 not in n: # detect start of sequence within set
                length = 1
                while value + length in n: # Increase length and find remainder of sequence
                    length += 1 

                longest = max(length, longest) # compare longest sequence with current

        return longest # return longest sequence that was found