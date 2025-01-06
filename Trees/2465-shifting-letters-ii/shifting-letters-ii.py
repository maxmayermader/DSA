class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Initialize difference array
        diff = [0] * (len(s) + 1)
        
        # Record shifts using difference array
        for start, end, direction in shifts:
            value = 1 if direction == 1 else -1
            diff[start] += value
            diff[end + 1] -= value
        
        # Calculate prefix sum
        for i in range(1, len(s)):
            diff[i] += diff[i-1]
        
        # Apply shifts to characters
        result = []
        for i in range(len(s)):
            # Calculate new position using modulo to handle wrapping
            new_pos = (ord(s[i]) - ord('a') + diff[i]) % 26
            result.append(chr(ord('a') + new_pos))
            
        return ''.join(result)

                














        # letters = [ord(c) for c in s] #a=97, z= 122
        
        # def getNewPos(cur, direc):
        #     if direc == 0:
        #         if cur - 1 < 97:
        #             return 122
        #         return cur - 1
        #     else:
        #         if cur + 1 > 122:
        #             return 97
        #         return cur + 1

        # for s, e, direc in shifts:
        #     for i in range(s, e+1):
        #         letters[i] = getNewPos(letters[i], direc)

        # res = ""
        # for letter in letters:
        #     res += chr(letter)

        # return res

        