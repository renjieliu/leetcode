class Solution:
    def sumOddLengthSubarrays(self, arr: 'List[int]') -> int:
        total = [arr[0]]
        for a in arr[1:]:
            total.append(total[-1] + a)
        output = 0
        for length in range(1, len(arr)+1, 2):
            for i in range(len(arr)-length+1):
                lastElement = i+length-1
                if i == 0:
                    output+=total[lastElement]
                else:
                    output+= total[lastElement] - total[i-1]
        return output