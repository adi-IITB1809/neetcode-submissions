class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m*n))

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False


        #O(m+logn)
        target_row = 0
        m= len(matrix)
        n= len(matrix[0])

        for i in range(m):
            if target<= matrix[i][n-1]:
                target_row= i
                break
            
            
        left = 0
        right = n-1

        while left<=right:
            mid = (left+right)//2
            if target==matrix[target_row][mid]:
                return True
            elif target<matrix[target_row][mid]:
                right= mid-1
            else:
                left = mid+1

        return False
        