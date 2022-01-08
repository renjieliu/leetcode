class Solution:
    def numberOfBeams(self, bank: 'List[str]') -> int:
        cnt = 0
        prev = 0
        for b in bank:
            curr = b.count('1') 
            cnt += prev * curr 
            prev = curr if curr else prev #if curr == 0, then no laser in current row, just keep the prev
        return cnt

    
