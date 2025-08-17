text="I am  a student "
from collections import defaultdict
import random

words=text.split()

markov_chain=defaultdict(list)

for i in range(len(words)-1):
    current_word=words[i]
    next_word=words[i+1]
    markov_chain[current_word].append(next_word)
    print(markov_chain)
