def canWinNim(n: int) -> bool:
    return not (n % 4 == 0)



print(canWinNim(12))