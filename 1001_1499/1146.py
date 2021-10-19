class SnapshotArray:

    def __init__(self, length: int):
        self.arr = {}
        for i in range(length):
             self.arr[i] = 0
        self.cnt = 0
        self.changed = {}
        self.arr_snapshot = {}


    def set(self, index: int, val: int):
        self.arr[index] = val
        self.changed[index] = val


    def snap(self):
        self.arr_snapshot[self.cnt] = self.changed.copy()
        self.cnt += 1
        return self.cnt-1


    def get(self, index: int, snap_id: int):
        return 0 if index not in self.arr_snapshot[snap_id] else self.arr_snapshot[snap_id][index]



# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0,5)
obj.snap()
obj.set(0,6)
print(obj.get(0,0))


