# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        hmp = {}  # key is power, val is the coefficient
        while poly1:
            if poly1.power not in hmp:
                hmp[poly1.power] = 0
            hmp[poly1.power] += poly1.coefficient
            poly1 = poly1.next
        while poly2:
            if poly2.power not in hmp:
                hmp[poly2.power] = 0
            hmp[poly2.power] += poly2.coefficient
            poly2 = poly2.next

        arr = []
        for k in sorted(hmp.keys(), reverse=True):
            if hmp[k] != 0:
                arr.append([k, hmp[k]])

        if arr == []:
            return None
        else:
            start = PolyNode(arr[0][1], arr[0][0])  # PolyNode(coefficient,power), reversed from the arr
            arr.pop(0)
            node = start
            while arr:
                node.next = PolyNode(arr[0][1], arr[0][0])
                arr.pop(0)
                node = node.next
            return start

