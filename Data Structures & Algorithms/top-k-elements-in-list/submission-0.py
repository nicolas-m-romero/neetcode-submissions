import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        count_num = []

        for key in count:
            heapq.heappush(count_num, (count[key], key))

        print(count_num)

        k_pairs = heapq.nlargest(k, count_num)

        output = []

        for i in range(len(k_pairs)):
            output += [k_pairs[i][1]]

        return output
