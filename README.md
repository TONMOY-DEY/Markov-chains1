Markov Chain Text Generator

A simple Python program to build a Markov chain from a given text. It maps each word to the list of words that can follow it, useful for text generation.

Features

Split text into words.

Build a Markov chain dictionary.

Print the chain step by step.

Requirements

Python 3.x

Usage
from collections import defaultdict
import random

text = "I am a student"
words = text.split()

markov_chain = defaultdict(list)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    markov_chain[current_word].append(next_word)
    print(markov_chain)

Example Output
defaultdict(<class 'list'>, {'I': ['am']})
defaultdict(<class 'list'>, {'I': ['am'], 'am': ['a']})
defaultdict(<class 'list'>, {'I': ['am'], 'am': ['a'], 'a': ['student']})

Future Improvements

Generate random sentences.

Handle punctuation and capitalization.

Support multi-word sequences (n-grams) for advanced text generation.
