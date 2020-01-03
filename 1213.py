class Solution:
    def arraysIntersection(self, arr1: 'List[int]', arr2: 'List[int]', arr3: 'List[int]') -> 'List[int]':
        t = [] #common number in arr1 and arr2
        output = [] #common for t and arr3
        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                arr1.pop(0)
            elif arr1[0] == arr2[0]:
                t.append(arr1.pop(0))
                arr2.pop(0)
            else:
                arr2.pop(0)

        while t and arr3:
            if arr3[0] < t[0]:
                arr3.pop(0)
            elif t[0] < arr3[0]:
                t.pop(0)
            else:
                output.append(t.pop(0))
                arr3.pop(0)
        return output