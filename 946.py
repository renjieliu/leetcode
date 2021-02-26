class Solution:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> bool:
        arr = []
        while pushed: #simulate the push and pop process, and see if all pushed can be pushed, and all popped can be popped
            arr.append(pushed.pop(0))
            while arr and arr[-1] == popped[0]:
                arr.pop()
                popped.pop(0)

        return pushed == popped == []

