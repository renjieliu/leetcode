class Solution:
    def merge(self, intervals: 'List[List[int]]') -> 'List[List[int]]':
        def overlap(A, B):
            if A[0] <= B[0] <= A[1]:  # B[0]<=A[0]<=A[1]<= B[1] or A[0]<=B[0]<=B[1]<=A[1] or B[0] <= A[0] <= B[1] or
                return 1
            return 0

        # for i in intervals: #no need to sort? Question raised to Leetcode and discussion board.
        #     i.sort()
        intervals.sort(key=lambda x: x[0])
        if len(intervals) <= 1:
            return intervals
        else:
            output = []
            j = 0
            while j < len(intervals):
                output.append(intervals[j])
                i = j + 1
                while i < len(intervals):  # check if there's overlapping with current output[-1]
                    if overlap(output[-1], intervals[i]) == 1:
                        output[-1] = [min(output[-1][0], intervals[i][0]), max(output[-1][1], intervals[i][1])]
                        j = i
                    elif intervals[i][0] > output[-1][1]:
                        break
                    i += 1
                j += 1
            return output








