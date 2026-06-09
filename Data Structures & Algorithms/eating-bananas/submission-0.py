class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Perform binary search on eating rate
        # to minimize the rate while eating all nanas
        minimum, maximum = 1, max(piles)
        output = maximum

        while minimum <= maximum:
            rate = (minimum + maximum) // 2

            # Traverse through piles
            # Calc how if can be eaten in time
            hours = 0

            for amount in piles:
                hours += math.ceil(amount / rate)

            # Compare hours to h (cap)
            if hours <= h:
                output = rate
                maximum = rate - 1
            else:
                minimum = rate + 1

        return output

