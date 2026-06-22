class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create (position, speed) pairs
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        # Sort pairs descending by position 
        # represents cars that are closest to target  
        pairs.sort(reverse=True)

        # Iterate through pairs
        output = []
        for p in pairs:
            # Calculate time to get to target
            duration = (target - p[0])/p[1]

            # If duration is less than one in front
            # will be forced to slow down to match duration
            # no need to add
            if output and duration <= output[-1]:
                continue

            output.append(duration)

        # Each index of output represents a group of cars
        return len(output)