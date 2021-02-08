class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
        people.sort(key = lambda x : x[0])
        output = [ [float('inf'),float('inf')] for _ in range(len(people)) ]
        #print(people)
        for height, c in people:
            cnt = 0
            for i in range(len(output)):
                if c == cnt and output[i][0] == float('inf'): #as long as a free slot, just to put it there
                    output[i] = [height, c]
                    break
                elif output[i][0] >= height:
                    cnt += 1
                #print(height,c , output )
        return output