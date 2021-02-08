class Codec:

    def __init__(self):
        self.decodeURL = {}
        self.encodeURL = {}
        self.maxID = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        shortURL = "http://a.com/" + str(self.maxID)
        self.encodeURL[longUrl] = shortURL
        self.decodeURL[shortURL] = longUrl
        self.maxID += 1
        return shortURL

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.decodeURL[shortUrl]

codec = Codec()
print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))



