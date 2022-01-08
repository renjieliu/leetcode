class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: 'List[int]') -> bool:
        asteroids.sort(reverse = True)
        while asteroids: 
            if mass >= asteroids[-1]: #keep adding the mass if it's >= current smallest
                mass+= asteroids.pop() # pop from the right side to speed up. pop(0) is slower than pop()
            else:
                return False
        return True
    

