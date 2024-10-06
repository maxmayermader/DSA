class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        # for word in strs:
        #     res += chr(300) + word + chr(299)
        for i in range(len(strs)):
            if i != len(strs)-1:
                res += strs[i] + chr(300)
            else:
                res += strs[i]

        print(res)

        return res
            

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []

        # for c in s:
        #     word = ""
            # while c != char()

        res = s.split(chr(300))
        print(res)

        return res
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))