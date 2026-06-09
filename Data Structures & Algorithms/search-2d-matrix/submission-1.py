class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Traverse rows
        left_r, right_r = 0, len(matrix) - 1

        while left_r <= right_r:
            middle_r = (right_r + left_r) // 2

            # Search within the row
            left_c, right_c = 0, len(matrix[middle_r]) - 1

            # Check if target within row
            if matrix[middle_r][left_c] <= target <= matrix[middle_r][right_c]:
                # Perform Binary Search on row
                while left_c <= right_c:
                    middle_c = (right_c + left_c) // 2

                    if matrix[middle_r][middle_c] == target:
                        return True
                    elif matrix[middle_r][middle_c] > target:
                        right_c = middle_c - 1
                    else:
                        left_c = middle_c + 1

                return False

            elif target > matrix[middle_r][right_c]:
                left_r = middle_r + 1
            else:
                right_r = middle_r - 1

        return False