from uzwords import words
from findMatches import findMatches
import random

# uzword.py ichidan 1ta tasodifiy so'z tanlaymiz
word = words[random.randint(0, len(words))]
print("Tasodifiy so'z: ", word)
print("Harflar: ", sorted(list(word)))

matches = findMatches(word, words)

print("Topilgan so'zlar: ", sorted(matches, key=len, reverse=True))

