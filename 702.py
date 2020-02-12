class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        i = 0
        while reader.get(i) != target:
            if reader.get(i) == 2147483647 or reader.get(i) > target:
                return -1
            i+=1
        return i