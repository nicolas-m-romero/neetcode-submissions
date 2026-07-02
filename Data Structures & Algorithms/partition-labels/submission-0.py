class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastAppearance = {} # map (letter: last seen index)

        for i, c in enumerate(s):
            lastAppearance[c] = i # update last seen index when seen

        # last occurence need to be precomputed to save from n^2 

        output = []
        size = end = 0 

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastAppearance[c]) # when hitting a new letter will adjust end to see last

            if i == end:
                output.append(size)
                size = 0
        
        return output
