class LockingTree:

    def __init__(self, parent: 'List[int]'):
        self.tree = parent

        self.p_node = {}
        for i, p in enumerate(parent):
            if p not in self.p_node:
                self.p_node[p] = []
            self.p_node[p].append(i)

        self.locked = {}
        #print(self.p_node)


    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False


    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False
        del self.locked[num]
        return True



    def upgrade(self, num: int, user: int) -> bool:
        def lockedC(p_node, locked, num): #check locked descendants
            if num in p_node:
                for c in p_node[num]:
                    if c in locked or lockedC(p_node, locked, c):
                        return True
            return False  # no descendants locked


        def lockedP(tree, locked, num): # check if there's locked ancestor
            while num != -1 and num not in locked:
                num = tree[num]
            return False if num == -1 and -1 not in locked else True

        def unlockC(p_node, locked, num): #unlock all the descendants
            if num in p_node:
                for c in p_node[num]:
                    if c in locked:
                        del locked[c]
                    unlockC(p_node, locked, c)


        if num in self.locked or lockedC(self.p_node, self.locked, num) == False or lockedP(self.tree, self.locked,num):
            # 1. itself not locked, 2. at least 1 descendant locked, 3. no parent locked
            return False
        else:
            unlockC(self.p_node, self.locked, num)
            self.locked[num] = user
            return True







# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)