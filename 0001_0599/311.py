class Solution:
    def multiply(self, mat1: 'List[List[int]]', mat2: 'List[List[int]]') -> 'List[List[int]]':        
        def helper(arr1, arr2): #calc the multi
            output = 0
            for i in range(len(arr1)):
                output+=arr1[i] * arr2[i]
            return output
        
        mat = []
        for c in range(len(mat2[0])): #transpose the mat2, to make the calc easier
            mat.append([])
            for r in range(len(mat2)):
                mat[-1].append(mat2[r][c])
                
        output=[]
        for r1 in mat1:
            output.append([])
            for r2 in mat:
                output[-1].append(helper(r1, r2))
        return output
                


