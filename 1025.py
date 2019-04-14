def divisorGame(N: int):
    if N%2==0 or N%6==0:
        return True
    else:
        return False


print(divisorGame(6))
print(divisorGame(3))
print(divisorGame(7))
print(divisorGame(9))
print(divisorGame(8))
print(divisorGame(10))