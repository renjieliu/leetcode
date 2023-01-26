class Solution:
    def sortTheStudents(self, score: 'List[List[int]]', k: int) -> 'List[List[int]]': # O( NlogN | N )
        arr = []
        for r in range(len(score)): # take out the kth exam
            arr.append([score[r][k], r]) # [score, rowNumber]
        arr.sort(key = lambda x: x[0], reverse = True)
        output = []
        for a in arr:
            output.append(score[a[1]]) # add the corresponding row to the output
        
        return output
    
