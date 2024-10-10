class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        # return s == s[::-1]
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         letters = []
#         if len(s) < 1 and s != " ":
#             return False
#         for char in s:
#             if char.isalpha():
#                 letters.append(char.lower())
#         if len(letters) == 0:
#             return True
#         if len(letters) == 1 and letters[0].isalpha():
#             return False
#         rev = letters.copy()
#         rev.reverse()
#         print(letters)

#         return letters == rev