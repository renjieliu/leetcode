class Solution:
    def rotateTheBox(self, box: 'List[List[str]]') -> 'List[List[str]]':
        def move(arr): #move the stone to the right, before rotate
            output = ["."] * len(arr)
            slots = []
            for i , a in enumerate(arr):
                if a == ".":
                    slots.append(i)
                elif a == "#":
                    if slots:
                        output[slots.pop(0)] = "#"
                        slots.append(i) #current pos is open as a slot, as the stone is moved
                    else:
                        output[i] = "#"
                elif a == "*":
                    output[i] = "*"
                    slots = []
            return output

        grid = []
        for b in box:
            grid.append(move(b[::-1])[::-1])

        #print(grid)

        def rotate(arr):
            output = [[None for r in range(len(arr))] for c in range(len(arr[0]))]
            for r in range(len(arr)):
                for c in range(len(arr[0])):
                    rotate_r = c
                    rotate_c = len(arr) - 1 - r
                    output[rotate_r][rotate_c] = arr[r][c]
            return output

        return rotate(grid)









