class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}:{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = s.find(':', i)
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result

# class Codec:
#     def encode(self, strs: List[str]) -> str:
#         """Encodes a list of strings to a single string.
#         """
#         res = ""
#         # for word in strs:
#         #     res += chr(300) + word + chr(299)
#         for i in range(len(strs)):
#             if i != len(strs)-1:
#                 res += strs[i] + chr(300)
#             else:
#                 res += strs[i]

#         print(res)

#         return res
            

        

#     def decode(self, s: str) -> List[str]:
#         """Decodes a single string to a list of strings.
#         """
#         res = []

#         # for c in s:
#         #     word = ""
#             # while c != char()

#         res = s.split(chr(300))
#         print(res)

#         return res
        
        


# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(strs))