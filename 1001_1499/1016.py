def queryString(S: str, N: int):
    for i in range(1,N+1):
        b = str(bin(i)).replace('0b', '')
        if S==S.replace(b,""):
            return False

    return True

print(queryString("0110", 3))
print(queryString(S = "0110", N = 4))