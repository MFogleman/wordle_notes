from functools import partial, reduce

WORDS = ["apple", "bands", "carat", "doggo", "eaten", "foxes", "goats", "hoppy", "kites", "lamer"]

def score_letters_by_count(words):
  d = {}
  for word in words:
    for letter in word:
      if letter in d.keys():
        d[letter] += 1
      else:
        d[letter] = 1
  return d

def score_word(score_val, word):
  return reduce(
    lambda score, letter: score + score_val[letter], 
    word,
    0
  )  


def cb(map, tup, word):
  top_word, top_score = tup
  new_score = score_word(map, word)
  if new_score > top_score:
    return (word, new_score)
  return (top_word, top_score)

def make_guess(words):
  d = score_letters_by_count(words)

  (top_word, top_score) = reduce(
    partial(cb, d),
    words,
    (None, 0)
  )
  print(f"top_score: {top_score}, top_word: {top_word}")


make_guess(WORDS) #top_score: 25, top_word: eaten
