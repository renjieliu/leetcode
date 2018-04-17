def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if n == 0:
        return True
    if n > len(flowerbed):
        return False
    elif len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
        return True
    elif len(flowerbed) == 1 and flowerbed[0] == 1 and n == 1:
        return False
    else:
        x = "`"
        for i in flowerbed:
            x += str(i)
        x += "|"
        currLen = len(x)
        x = x.replace("`00", "10").replace("00|", "01")
        while x.find("000") != -1:
            x = x.replace("000", "0$0")
        return True if currLen - len(x.replace("$", "")) >= n else False


print(canPlaceFlowers( [1,0,0,0,0,0,1], 2 ))
print(canPlaceFlowers( [0,0,1,0,1], 1 ))




