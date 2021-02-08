class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        def square(m, output): #calculate the outmost layer
            output += m[0] #first row
            for r in range(1, len(m)-1):#last col
                output.append(m[r][-1])
            output += m[-1][::-1] # last row
            for r in range(len(m)-2, 0, -1): #first column
                output.append(m[r][0])

        t = matrix.copy()
        output = []
        while t != []: # each time, take out the outmost layer. And iterate through to the last(inner most) element
            if len(t) ==1 :
                output+= t[0] #first row
                return output
            elif len(t[0]) ==0:
                return output
            elif len(t[0]) == 1:
                output+= map(lambda x: x[0], t)
                return output
            else:
                square(t, output)
                x = t.copy()
                t = []
                for r in range(1, len(x)-1):
                    t.append([])
                    for c in range(1, len(x[0])-1):
                        t[-1].append(x[r][c])
        return output