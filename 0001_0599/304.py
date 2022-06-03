class NumMatrix:

    def __init__(self, matrix: 'List[List[int]]'): #O(MN | MN)
        self.arr = [] # store the accumulated sum for each row
        for r in matrix: 
            self.arr.append([0]) #preceding 0, to simplify the calc logic sa
            for c in range(len(r)):
                self.arr[-1].append(self.arr[-1][-1] + r[c])
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: #O(N | 1)
        total = 0
        for r in range(row1, row2+1):
            total += self.arr[r][col2+1] - self.arr[r][col1+1-1] # the col + 1 , for the preceding 0 in front of each row
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



# previous solution

# class NumMatrix:

#     def __init__(self, matrix: 'List[List[int]]'):
#         self.arr = []
#         for r in matrix:
#             self.arr.append([0])
#             for c in r:
#                 self.arr[-1].append(self.arr[-1][-1] + c)



#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         stk = []
#         for r in range(row1, row2+1):
#             stk.append(self.arr[r][col2+1] - self.arr[r][col1])
#         return sum(stk)


# # Your NumMatrix object will be instantiated and called as such:
# # obj = NumMatrix(matrix)
# # param_1 = obj.sumRegion(row1,col1,row2,col2)


