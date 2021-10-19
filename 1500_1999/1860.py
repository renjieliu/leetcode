class Solution:
    def memLeak(self, memory1: int, memory2: int) -> 'List[int]':
        curr = 1
        time = 1
        while memory1>=curr or memory2 >=curr:
            time += 1
            if memory1>=memory2:
                memory1-=curr
            else:
                memory2-=curr
            curr += 1
        return [time, memory1, memory2]


