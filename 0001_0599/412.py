def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    output = list()
    for i in range(1, n+1):
        item = str(i)
        if i%3==0:
            item = "Fizz"
        if i % 5 == 0:
            item = "Buzz"
        if i%15 ==0:
            item = "FizzBuzz"

        output.append(item)

    return output

print(fizzBuzz(15))