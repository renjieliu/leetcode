class Solution:
    def atMostNGivenDigitSet(self, digits: 'List[str]', n: int) -> int:
        output = [0]
        for i in range(1, len(str(n))):  # for the first x-1 digits, pick any from the nums..
            output[0] += (len(digits) ** i)
        # print(output)
        digits.sort()

        def helper(output, target, arr):  # iterate through each digit. if <, same as above,  if == check the rest
            for i, d in enumerate(arr):  # to calculate the same length
                if d < target[0]:
                    output[0] += (len(arr) ** (len(target) - 1))
                elif d == target[0]:
                    if len(target[1:]) == 0:
                        output[0] += 1
                    else:
                        helper(output, target[1:], arr)
                elif d > target[0]:
                    break

        helper(output, str(n), digits)

        return output[0]
