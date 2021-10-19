def distributeCandies(candies: int, num_people: int):
    left = candies
    output = [0]*num_people
    curr = 1
    while 1:
        for i in range(num_people):
            if left >= curr:
                output[i]+=curr

            else:
                output[i] += left
                return output
            left -=curr
            curr+=1


print(distributeCandies(candies = 7, num_people = 4))
print(distributeCandies(candies = 10, num_people = 3))