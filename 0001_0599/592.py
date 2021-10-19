class Solution:
    def fractionAddition(self, expression: str) -> str:  # assume the final result is A/B.
        def gcd(a, b):  # find the Greatest Common divisor
            x = a if a >= b else b
            y = b if x == a else a
            # print(a,b)
            mod = x % y
            while mod != 0:
                x = y
                y = mod
                mod = x % y
            return y

        def lcm(a, b):  # find the least common multiple
            t = gcd(a, b)
            return t * (a // t) * (b // t)

        expression = expression.replace('-', '+-')
        parts = expression.split('+')  # all the individual part would be in the form of 'A/B'
        A = []
        B = []
        for p in parts:
            if len(p) > 0:
                A.append(int(p.split('/')[0]))
                B.append(int(p.split('/')[1]))
        if len(B) < 2:
            g = gcd(abs(A[0]), abs(B[0]))  # find the GCD, and make the A and B  irreducible
            return str(A[0] // g) + "/" + str(B[0] // g)
        else:
            t = lcm(B[0], B[1])
            i = 2
            while i < len(B):
                t = lcm(t, B[i])
                i += 1
            i = 0
            while i < len(A):  # calculate the A
                A[i] = (t // B[i]) * A[i]
                i += 1
            top = sum(A)
            bottom = t
            if top / bottom == top // bottom:
                return str(top // bottom) + '/1'
            else:
                g = gcd(abs(top), abs(bottom))
                return str(top // g) + '/' + str(bottom // g)


