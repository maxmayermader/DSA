# class Codec:
#     def __init__(self):
#         self.urls = {}
#         self.urlNum = 0


#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         newUrl = "http://tinyurl.com/"+str(self.urlNum)
#         self.urlNum+=1
#         self.urls[newUrl] = longUrl
#         return newUrl

        

#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return self.urls[shortUrl]

        

# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(url))
class Codec:
    def __init__(self):
        self.encodeurl = {}
        self.decodeurl = {}

        self.baseurl = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeurl:
            shortUrl = self.baseurl + str(len(self.encodeurl))
            self.encodeurl[longUrl] = shortUrl 
            self.decodeurl[shortUrl] = longUrl
        return self.encodeurl[longUrl]

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeurl[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))