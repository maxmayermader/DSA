class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0

        while i < len(haystack):
            if haystack[i] == needle[0]:
                j=i
                k = 0
                while j < len(haystack) and k < len(needle) and haystack[j] == needle[k]:
                    j +=1
                    k+=1
                if haystack[i:j] == needle:
                        return i
            i += 1
            j = i
                
        return -1

        