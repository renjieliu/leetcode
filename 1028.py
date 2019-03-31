def baseNeg2(N: int):
    if N == 0:
        return "0"

    else:
        output = ""
        while N != 0:
            curr = N % (-2)

            N //= -2

            if curr < 0: #if the remainder is negative, add the base *-1 to it add 1 to the current N.
                curr += 2
                N += 1

            output = str(curr) + output

    return output


print(baseNeg2(4))
print(baseNeg2(2))
print(baseNeg2(3))
