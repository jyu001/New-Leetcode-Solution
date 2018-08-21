'''
535. Encode and Decode TinyURL
DescriptionHintsSubmissionsDiscussSolution
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


'''

class Codec:
    def __init__(self):
        self.dct = {}
        self.dct2 = {}
        self.count = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.dct: 
            self.dct[longUrl] = self.count
            self.dct2[self.count] = longUrl
            self.count += 1
        return 'http://tinyurl.com/'+str(self.dct[longUrl])
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dct2[int(shortUrl[19:])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))