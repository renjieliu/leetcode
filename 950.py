def deckRevealedIncreasing(deck: 'List[int]'):
    output  = []
    deck.sort()
    for i in deck[::-1]:
        output.insert(0,i)
        output.insert(1, output.pop())
    return output


print(deckRevealedIncreasing ([17,13,11,2,3,5,7]))