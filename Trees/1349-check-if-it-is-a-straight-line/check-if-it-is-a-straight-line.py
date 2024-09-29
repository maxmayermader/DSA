class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # slopex = abs(coordinates[1][0] - coordinates[0][0])
        # slopey = abs(coordinates[1][1] - coordinates[0][1])

        # for i in range(len(coordinates)-1):
        #     if coordinates[i][0] + slopex != coordinates[i+1][0] or coordinates[i][1] + slopey != coordinates[i+1][1]:
        #         return False

        # return True
        def getXDiff(p1, p2):
            return p2[0]-p1[0]
        def getYDiff(p1, p2):
            return p2[1]-p1[1]

        xDiff = getXDiff(coordinates[0], coordinates[1])
        yDiff = getYDiff(coordinates[0], coordinates[1])

        for i in range(2, len(coordinates)):
            if (yDiff * getXDiff(coordinates[i], coordinates[0]) 
            != xDiff * getYDiff(coordinates[i], coordinates[0])):
                return False

        return True