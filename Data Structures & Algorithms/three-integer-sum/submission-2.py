class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        output = []

        for j in range(1, len(n) - 1):
            i = 0
            k = len(n) - 1

            # - n[j] = n[i] + n[k] where n[i] < n[j] < n[k]
            # therefore, if n[i] + n[k] > -n[j], then k--
            # and, if n[i] + n[k] < -n[i], then i++
            # also i < j < k
            while i < j < k:
                if n[i] + n[k] == -n[j]:
                    if [n[i], n[j], n[k]] not in output:
                        output.append([n[i], n[j], n[k]])
                    k -= 1 # Change one end arbitrarily to see new combintions
                elif n[i] + n[k] > -n[j]:
                    k -= 1
                elif n[i] + n[k] < -n[j]:
                    i += 1

        return output
