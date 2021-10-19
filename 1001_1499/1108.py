def defangIPaddr(address: str):
    return address.replace('.','[.]')


print(defangIPaddr(address = "1.1.1.1"))
print(defangIPaddr(address = "255.100.50.0"))



