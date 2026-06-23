class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0 

        while i < len(nums) - 2 and nums[i] <= 0:
            j, k = i + 1, len(nums) - 1

            while j < k:
                triplet = nums[i] + nums[j] + nums[k]
                if triplet == 0:
                    if [nums[i], nums[j], nums[k]] not in output:
                        output.append([nums[i], nums[j], nums[k]])
                    k -= 1
                elif triplet > 0:
                    k -= 1
                elif triplet < 0:
                    j += 1

            i += 1

        return output
