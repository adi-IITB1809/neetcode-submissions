class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
        