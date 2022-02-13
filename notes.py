from functools import reduce

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

def make_guess(words):
  d = score_letters_by_count(words)
  top_word = None
  top_score = 0
  for word in words:
    new_score = score_word(d, word) 
    if  new_score > top_score:
      top_word = word
      top_score = new_score
  print(f"top_score: {top_score}, top_word: {top_word}")

make_guess(WORDS)
