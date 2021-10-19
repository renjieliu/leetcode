class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        minStk = [warehouse[0]]  # minHeight on the left
        for i in range(1, len(warehouse)):
            minStk.append(min(minStk[-1], warehouse[i]))
        cnt = 0
        boxes.sort()
        for m in minStk[::-1]:  # to check if there's boxes can be pushed from the left
            if boxes[0] <= m:
                cnt += 1
                boxes.pop(0)
                if len(boxes) == 0:
                    return cnt
        return cnt

