class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        l = 0
        r = (num_rows * num_cols) - 1

        while l <= r:
            mid = (l+r) // 2
            row_index = mid // num_cols
            col_index = mid % num_cols
            
            mid_num = matrix[row_index][col_index]

            if mid_num == target:
                return True
            elif mid_num < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
