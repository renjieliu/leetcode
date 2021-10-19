def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """

    if ord(letters[-1]) <= ord(target):
        return letters[0]
    else:
        for i in letters:
            if ord(i) - ord(target) > 0:
                return i

print(nextGreatestLetter(["c", "f", "j"], 'k'))
print(nextGreatestLetter(["c", "f", "j"], 'a'))
print(nextGreatestLetter(["c", "f", "j"], 'c'))
print(nextGreatestLetter(["c", "f", "j"], 'd'))
print(nextGreatestLetter(["c", "f", "j"], 'g'))
print(nextGreatestLetter(["c", "f", "j"], 'j'))
print(nextGreatestLetter(["c", "f", "j"], 'k'))

