class Solution:
    def minSpeedOnTime(self, dist: 'List[int]', hour: float) -> int:
        if int(hour) < len(dist)-1 or (hour == int(hour) and hour == len(dist)-1): #can't move at last hour
            return -1

        ceiling = lambda x: int(x) if x <= 0 or int(x)==x else int(x)+1
        def valid(arr, speed, target): # with speed, it can reach the office within target time
            total = 0
            for distance in arr[:-1]:
                total += ceiling(distance/speed)
            total += arr[-1]/speed
            return total <= target

        s = 1
        e = 10**7 #as suggested by the problem description
        output = e
        while s <= e: # binary search to find the min speed
            mid = s - (s-e)//2
            if valid(dist, mid, hour):
                output = min(output, mid)
                e = mid-1
            else:
                s = mid + 1
        return output


