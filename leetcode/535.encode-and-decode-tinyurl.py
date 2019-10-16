from string import ascii_letters, digits

digits_letters = digits + ascii_letters

class Codec:
    def __init__(self):
        self.mapping = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        i = len(self.mapping)
        code = ''
        while i:
            shang, i = divmod(i, 62)
            code += digits[shang]
        while len(code) < 6:
            code = '0'+code

        self.mapping[code] = longUrl
        return 'http://tinyurl.com/'+code
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        code = shortUrl[-6:]
        return self.mapping[code]

# Your Codec object will be instantiated and called as such:
codec = Codec()
long_url = 'https://leetcode.com/problems/design-tinyurl'
short_url = codec.encode(long_url)
print(short_url)
decoded_long_url = codec.decode(short_url)
print(decoded_long_url)
        