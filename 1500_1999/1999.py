class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        if digit1 == digit2 == 0 or set( ((k%10) * _)%10  for _ in range(1, 10)) & {digit1, digit2} == set():
            #d1 and d2 are not a multiple of last digit of k
            return -1

        def cross(A, B): #[digit1, digit2], Total
            output = []
            for a in A:
                for b in B:
                    output.append(b + [a])
                    output.append([a] + b)
            return output

        digit1 = str(digit1)
        digit2 = str(digit2)
        itr = 1
        prev = [[],[digit1, digit2]]
        output = [[],[digit1, digit2]]
        while itr < 9: # to find all the possible numbers < 2*31 - 1
            prev = cross([digit1, digit2], prev)
            output += prev
            itr+= 1

        output = list(set(tuple(o) for o in output))

        pool = sorted([int("".join(_)) for _ in output if _])
        # print(pool[-1])
        # print(pool)
        for p in pool:
            if p > 2**31-1:
                return -1
            if p%k == 0 and p > k and p <= 2**31-1 :
                return p
        return -1





