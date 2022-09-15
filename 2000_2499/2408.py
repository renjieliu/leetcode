class SQL:

    def __init__(self, names: 'List[str]', columns: 'List[int]'):
        self.tables = {}
        self.ID = {} # to record the current ID of the table.
        for i, n in enumerate(names):
            self.ID[n] = 0 
            self.tables[n] = {} # initiate table 
       

    def insertRow(self, name: str, row: 'List[str]') -> None: # O( N | N )
        self.ID[name] += 1 #get the current rowId
        rowID = self.ID[name]
        self.tables[name][rowID] = []
        for r in row:  #add the row to the hash table + rowId
            self.tables[name][rowID].append(r)
        

    def deleteRow(self, name: str, rowId: int) -> None: # O( 1 | 1 )
        del self.tables[name][rowId]
        

    def selectCell(self, name: str, rowId: int, columnId: int) -> str: # O( 1 | 1 )
        # print(self.tables, name, rowId, columnId)
        return self.tables[name][rowId][columnId-1] #column is arr, so return columnId-1
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)


