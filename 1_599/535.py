class Codec:

    def __init__(self):
        self.hmp_decoding = {}
        self.cnt = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.cnt += 1
        self.hmp_decoding[str(self.cnt)] = longUrl
        return str(self.cnt)


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hmp_decoding[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
