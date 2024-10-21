class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, rr = 0, len(matrix) - 1
        rm = 0
        while rl <= rr:
            rm = rl + ((rr-rl )// 2)
            if matrix[rm][0] <= target <= matrix[rm][-1]:
                break
            if matrix[rm][0] > target:
                rr = rm - 1
            else:
                rl = rm + 1

        l, r = 0, len(matrix[rm])-1
        while l <= r:
            m = l + ((r-l)//2)
            if matrix[rm][m] == target:
                return True
            if matrix[rm][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False