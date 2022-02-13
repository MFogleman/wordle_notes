from functools import partial, reduce
from collections import Counter

def sortDictByVal(d):
  return sorted(d, key = lambda k: d[k], reverse=True)

WORDS = ["apple", "bands", "carat", "doggo", "eaten", "foxes", "goats", "hoppy", "kites", "lamer"]

LETTER_SCORE_MAP = Counter(''.join(WORDS))
print(f"LETTER_SCORE_MAP: {LETTER_SCORE_MAP}")

def make_word_score_map(words):
  return reduce(
    lambda o, word: {**o, word: sum([LETTER_SCORE_MAP[letter] for letter in set(word)])},
    words,
    {}
  )
def make_guess(words):
  word_score_map = make_word_score_map(words)
  print(f"word_score_map: {word_score_map}")
  sorted_words = sortDictByVal(word_score_map)

  print(f"have sorted_words:{sorted_words}")

make_guess(WORDS) #top_score: 25, top_word: eaten

