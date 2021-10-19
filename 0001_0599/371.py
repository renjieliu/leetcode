def getSum(a: int, b: int) -> int:
    mask = 0xffffffff
    while a & mask != 0:
        carry = a & b  # compute the carry
        b = a ^ b  # perform the actual +
        a = carry << 1  # shift the carry for one bit, used for the next calculation

    return b & mask if a > mask else b


print(getSum(-1, 1))