class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        hmp_a = defaultdict(int)
        hmp_b = defaultdict(int)
        for c in a: hmp_a[c] +=1
        for c in b: hmp_b[c] +=1
        change_to_same = (len(a)- max(hmp_a.values())) + (len(b) - max(hmp_b.values()))

        s = float('inf')
        move_a = len(a) #total can be moved
        move_b = 0
        for pivot in range(97, 97+25): # make every letter of a to the pivot, and to the right of pivot for b
            move_a -= hmp_a[chr(pivot)]
            move_b += hmp_b[chr(pivot)]
            s = min(s, move_a + move_b)

        move_a = 0
        move_b = len(b) #total can be moved

        for pivot in range(97, 97+25):
            move_a += hmp_a[chr(pivot)]
            move_b -= hmp_b[chr(pivot)]
            s = min(s, move_a+move_b)

        return min(s, change_to_same)




















