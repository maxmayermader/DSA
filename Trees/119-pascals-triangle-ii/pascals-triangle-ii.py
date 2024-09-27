class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[] for _ in range(rowIndex+1)]#for _ in range(rowIndex+1)]
        for i in range(0,rowIndex+1):
            print(triangle)

            for j in range(0,i+1):
                if j != 0 and j != i:
                    triangle[i].append(triangle[i-1][j-1]+triangle[i-1][j])
                    continue

                triangle[i].append(1)


        print(triangle)
        return triangle[rowIndex]
        