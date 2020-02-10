class Solution:
    def smallestCommonElement(self, mat: 'List[List[int]]') -> int:
        def overlap(A,B):
            output = []
            i = 0
            while B: #B is the longer one
                if A == [] or B[0] > A[-1]: #in the sorted B and A, current B is larger than the max of A. No need to continue
                    break
                elif B[0] > A[0]:
                    A.pop(0)
                elif B[0] < A[0]:
                    B.pop(0)
                else:
                    output.append(A[0])
                    A.pop(0)
                    B.pop(0)
            return output
        output = []
        if len(mat) ==1:
            return mat[0][0]
        else:
            output = overlap(mat[0], mat[1])
            c = 2
            while c < len(mat):
                output = overlap(output, mat[c])
                if output == []: # no need to check the rest
                    return -1
                c+=1
            return -1 if output==[] else output[0]