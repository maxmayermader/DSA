class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        
        lr = 0
        rr = R-1
        
        while lr <= rr:
            mr = lr + ((rr - lr) // 2)
            if matrix[mr][0] <= target <= matrix[mr][C-1]:
                break
            elif matrix[mr][0] > target:
                rr = mr - 1
            else:
                lr = mr + 1
        print(mr)   
        l = 0
        r = C - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[mr][m] == target:
                return True
            elif matrix[mr][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
            
