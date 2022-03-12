#This program outputs all permutations of a given word

from itertools import permutations

def Permute(word):
    outcomes = [''.join(w) for w in permutations(word)]
    print(outcomes)
Permute("Rono")