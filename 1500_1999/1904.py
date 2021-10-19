class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        start = 3600*int(startTime[:2]) + 60*int(startTime[-2:]) #turn the start and end to seconds
        end = 3600*int(finishTime[:2]) + 60*int(finishTime[-2:])
        rounds = [900*i for i in range(24*4+1)] #all full rounds starting time in seconds
        if end < start: #if played overnight, split into before and after mid night
            arr = [[start, 24*3600], [0, end]]
        else:
            arr = [[start, end]]

        def countRounds(arr, rounds):
            s = -1
            for r in rounds: #get first round start
                if arr[0]<=r<=arr[1]:
                    s = r
                    break
            if s == -1 : # no full round start found
                return 0
            else:
                return (arr[1] - s)//900 #check how many full rounds in between
        output = 0
        for a in arr:
            output += countRounds(a, rounds)
        return output



