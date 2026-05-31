class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            difference = right - left
            computed_water = min(heights[left], heights[right]) * difference

            if computed_water >  max_water:
                max_water = computed_water

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water