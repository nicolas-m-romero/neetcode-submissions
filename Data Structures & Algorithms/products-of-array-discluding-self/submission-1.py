class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_p = product_s = 1
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = [1] * len(nums)

        i = 0
        j = len(nums) - 1

        while i < len(nums):
            prefix[i] = product_p
            product_p *= nums[i]

            suffix[j - i] = product_s
            product_s *= nums[j - i]

            i += 1

        for k in range(len(nums)):
            output[k] = prefix[k] * suffix[k]

        return output
