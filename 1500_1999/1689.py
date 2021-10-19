class Solution:
    def minPartitions(self, n: str) -> int: #just need to find the max of the string, as others can be tweaked to 0
        return int(max(n))