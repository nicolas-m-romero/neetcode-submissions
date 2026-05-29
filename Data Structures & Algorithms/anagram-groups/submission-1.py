class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for s in strs:
            sorted_list = sorted(s)
            sorted_string = "".join(sorted_list)

            if sorted_string not in output:
                output[sorted_string] = [s]
            else:
                output[sorted_string] += [s]

        return list(output.values())
        