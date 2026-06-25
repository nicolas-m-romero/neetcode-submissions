class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) - 1

        # Binary Search through rows to find row (possibly) containing target
        while l_row <= r_row:
            m_row = (l_row + r_row) // 2

            if matrix[m_row][0] <= target <= matrix[m_row][-1]: # target is within range of row
                # perform binary search within row in search of target
                l, r = 0, len(matrix[m_row]) - 1

                while l <= r:
                    m = (l + r) // 2

                    if matrix[m_row][m] == target: # target found
                        return True
                    elif matrix[m_row][m] < target: # middle less than target
                        l = m + 1
                    else: # middle greater than target
                        r = m - 1

                return False # target was within range of row, but not present

            elif matrix[m_row][-1] < target: # target is greater than largest value in row
                l_row = m_row + 1
            else: # target is less than smallest value in row
                r_row = m_row - 1

        # target was not found within the 
        return False

