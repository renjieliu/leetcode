class Solution:
    def dividePlayers(self, skill: 'List[int]') -> int: # O( N | N )
        counter = {}  #record the occurrence of each number
        total = 0
        for s in skill:
            total += s
            if s not in counter:
                counter[s] = 0
            counter[s] += 1 


        target = total // (len(skill) // 2)
        output = 0 
        if target%2 == 0 and target // 2 in counter: # target = a+a
            if counter[target//2] % 2:
                return -1 
            else:
                groups = counter[target//2]//2 
                output += groups * ( (target//2) **2)
                del counter[target//2]

        lst = list(counter.keys())
        for n in lst: # to find the counterpart
            if n in counter: # not seen before
                if target-n not in counter or counter[n] != counter[target-n]:
                    return -1
                else: 
                    output += (n * (target-n)) * counter[n]
                    del counter[n]
                    del counter[target-n]

        return output



