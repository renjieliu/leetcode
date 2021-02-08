def intToRoman(num: 'int'):
    map = { 1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
           }
    map_key =[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    output = ""
    while num >0:
        for i in map_key:
            if num//i != 0:
                output+= map[i]*(num//i)
                num-= i * (num//i)

    return output

print(intToRoman(10))
print(intToRoman(99))
print(intToRoman(3999))
print(intToRoman(2019))
print(intToRoman(1231))












