class Solution:
    def trimMean(self, arr: 'List[int]') -> float:
        arr.sort()
        take = int(len(arr) * 0.05)
        return sum(arr[take:-take]) / len(arr[take:-take])
