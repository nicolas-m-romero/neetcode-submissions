class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum, maximum = 1, max(piles) # optimal: 1 < k < max(piles)
        output = maximum # starts at highest eating rate

        while minimum <= maximum:
            k = (minimum + maximum) // 2

            hours = 0
            for p in piles: # Calc total time to eat all bananas
                hours += math.ceil(float(p) / k)

            if hours <= h: # all bananas eaten in time
                output = k 
                maximum = k - 1 # decrease max to see smaller k
            else:
                minimum = k + 1 # increase min to see larger k

        return output
