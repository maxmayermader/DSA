class Codec:
    def __init__(self):
        self.urls = {}
 
        self.base = "http://tinyurl.com/"


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # newUrl = "http://tinyurl.com/"+str(self.urlNum)
        newUrl = self.base+str(len(longUrl))
        self.urls[newUrl] = longUrl
        # self.urlNum+=1
        return newUrl

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))