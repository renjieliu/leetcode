class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.zeroes = set(_ for _ in range(self.size)) # record the location of 0
        self.ones = set() # record the location of 1


    def fix(self, idx: int) -> None: 
        if idx in self.zeroes:
            self.zeroes.remove(idx)
        self.ones.add(idx)

        

    def unfix(self, idx: int) -> None:
        if idx in self.ones:
            self.ones.remove(idx)
        self.zeroes.add(idx)

        

    def flip(self) -> None: #swap the location of 0 and 1 
        t = self.ones
        self.ones = set()
        self.ones = self.zeroes
        self.zeroes = set()
        self.zeroes = t

        

    def all(self) -> bool:
        return self.zeroes == set()
        
    def one(self) -> bool:
        return len(self.ones) > 0
        

    def count(self) -> int:
        return len(self.ones)
        
    def toString(self) -> str:
        output = "" 
        for i in range(self.size):
            output+="1" if i in self.ones else "0"
        return output

        
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()


