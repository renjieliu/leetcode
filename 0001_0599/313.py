class Solution:
    def nthSuperUglyNumber(self, n: int, primes: 'List[int]') -> int:
        if n in [0, 1]:
            return n
        else:
            curr = [0] * len(primes)  # to mark which number from the output list should curr prime starts iterating.
            output = [1]
            while len(output) < n:
                temp = float('inf')
                for i in range(len(primes)):
                    temp = min(temp, primes[i] * output[curr[i]])
                output.append(temp)

                for j in range(len(curr)):
                    while primes[j] * output[curr[j]] <= output[
                        -1]:  # the start point should be greater than the last added number
                        curr[j] += 1

            return output[-1]