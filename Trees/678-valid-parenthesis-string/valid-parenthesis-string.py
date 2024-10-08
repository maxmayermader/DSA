class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, rightMax = 0,0

        for c in s:
            if c == '(':
                leftMin += 1
                rightMax += 1
            elif c == ')':
                leftMin -= 1
                rightMax -= 1
            else:
                leftMin -= 1
                rightMax += 1
            if rightMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
            
        return leftMin == 0