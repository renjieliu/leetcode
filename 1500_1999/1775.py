class Solution:
    def minOperations(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
        if sum(nums1) == sum(nums2):
            return 0
        elif len(nums1) > len(nums2) *6 or len(nums1) *6 < len(nums2):
            return -1
        else:
            a = nums1 if sum(nums1) < sum(nums2) else nums2 # a <= b
            b = nums2 if a == nums1 else nums1
            sum_a = sum(a)
            sum_b = sum(b)
            cnt = 0
            a.sort()
            b.sort()
            while a and b and sum_a < sum_b:
                A = a[0] #from least to most
                B = b[-1] #from most the least
                if (6 - A) > (B-1) : #each time, change the item that will have the most gain
                    sum_a += (6 - A)
                    cnt += 1 if A < 6 else 0
                    a.pop(0)
                else:
                    sum_b -= (B-1)
                    cnt +=1 if B > 1 else 0
                    b.pop()

            while b and sum_a<sum_b: #it's possible a is exhausted , but b still has some left
                B = b.pop()
                sum_b -= (B-1)
                cnt +=1 if B > 1 else 0

            while a and sum_a<sum_b: # it's possible b is exhausted, but a still has some left.
                A = a.pop(0)
                sum_a += (6 - A)
                cnt += 1 if A < 6 else 0

            return cnt

















