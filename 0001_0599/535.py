class Codec:
    
    def __init__(self): #O(1 | 1)
        self.num = 0 
        self.lkp = {}

    def encode(self, longUrl: str) -> str: #O(1 | 1)
        """Encodes a URL to a shortened URL.
        """
        self.num += 1 
        self.lkp[str(self.num)] = longUrl
        return str(self.num)
        
        

    def decode(self, shortUrl: str) -> str: #O(1 | 1)
        """Decodes a shortened URL to its original URL.
        """
        return self.lkp[str(shortUrl)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))




# previous solution

# class Codec:

#     def __init__(self):
#         self.hmp_decoding = {}
#         self.cnt = 0

#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         self.cnt += 1
#         self.hmp_decoding[str(self.cnt)] = longUrl
#         return str(self.cnt)


#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return self.hmp_decoding[shortUrl]


# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(url))




# previous solution

# class Codec:
    
#     def __init__(self):
#         self.decodeURL = {}
#         self.encodeURL = {}
#         self.maxID = 0
        
#     def encode(self, longUrl):
#         """Encodes a URL to a shortened URL.
        
#         :type longUrl: str
#         :rtype: str
#         """
#         shortURL = "http://a.com/" + str(self.maxID)
#         self.encodeURL[longUrl] = shortURL
#         self.decodeURL[shortURL] = longUrl
#         self.maxID+=1
#         return shortURL

        
#     def decode(self, shortUrl):
#         """Decodes a shortened URL to its original URL.
        
#         :type shortUrl: str
#         :rtype: str
#         """
#         return self.decodeURL[shortUrl]
        
        
        
        
        

# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(url))