class SubrectangleQueries:

    def __init__(self, rectangle: 'List[List[int]]'):
        self.rec = rectangle
        self.updates = []  #update stack

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append([row1 , col1 , row2 , col2 , newValue])
#         for r in range(row1, row2+1):
#             for c in range(col1, col2+1):
#                 self.rec[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        for i in self.updates[::-1]:
            if i[0]<=row<=i[2] and i[1]<=col<=i[3]:
                return i[4]
        return self.rec[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)