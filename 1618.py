# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
# class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
#
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: 'List[int]', fontInfo: 'FontInfo') -> int:
        def fits(f, text, w, h):
            hmp = {}
            for i in range(97, 123):  # check the width for each letter, put into a hmp to lookup
                hmp[chr(i)] = fontInfo.getWidth(f, chr(i))
            totalWidth = sum([hmp[c] for c in text])
            height = fontInfo.getHeight(f)
            return True if totalWidth <= w and height <= h else False

        s = 0
        e = len(fonts) - 1
        output = -1
        while s <= e:
            mid = s - (s - e) // 2
            if fits(fonts[mid], text, w, h) == True:
                s = mid + 1
                output = mid
            else:
                e = mid - 1
        return fonts[output] if output != -1 else -1











