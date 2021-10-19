class FileSharing:

    def __init__(self, m: int):
        self.m_owner = {}  # owner list for each chunk
        self.oldID = []  # people left
        self.currID = 0  # current ID generator
        self.owner = {}  # the chunk owned by the ID

    def join(self, ownedChunks: 'List[int]') -> int:
        if self.oldID:  # if we have something in the oldID, take the smallest one.
            # res = self.oldID.pop(0)
            res = heapq.heappop(self.oldID)
        else:
            self.currID += 1
            res = self.currID

        for o in ownedChunks:  # add them to the owner
            if o not in self.m_owner:
                self.m_owner[o] = set()
            self.m_owner[o].add(res)
        self.owner[res] = set(ownedChunks)
        return res

    def leave(self, userID: int) -> None:
        heapq.heappush(self.oldID, userID)
        for o in self.owner[userID]:
            self.m_owner[o].remove(userID)
            if len(self.m_owner[o]) == 0:
                del self.m_owner[o]
        del self.owner[userID]

    def request(self, userID: int, chunkID: int) -> 'List[int]':
        if chunkID not in self.m_owner:  # no one owns the current chunk
            return []
        else:
            res = sorted(list(self.m_owner[chunkID]))
            self.m_owner[chunkID].add(userID)
            self.owner[userID].add(chunkID)
            return res

# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)