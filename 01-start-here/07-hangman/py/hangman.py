#!/usr/bin/env python3
import random

MAX_MISSES = 6
WORDS = ["hamburger", "hot dog", "pizza", "taco", "spaghetti", "sushi", "salad", "sandwich", "omelette", "pancake"]

def main():
  # Select a word...
  word = WORDS[random.randrange(0, len(WORDS))]

  # Create a blank answer...
  answer = create_blank_answer(word)

  # Tracked missed answers...
  misses = 0
  while None in answer and misses < MAX_MISSES:
    draw_screen(misses, answer)
    next_letter = input("What letter would you like to try next?\n").lower().strip()
    if len(next_letter) != 1 or not next_letter.isalpha():
      print("Please enter a single letter (a-z).")
      continue
    if next_letter in word:
      for i in range(0, len(word)):
        if word[i] == next_letter:
          answer[i] = next_letter
    else:
      misses += 1
  else:
    draw_screen(misses, answer)
    if None not in answer:
      print("You win! You saved the man!")
    else:
      print("Welp, better luck next time.")

def is_victory(answer):
  return None not in answer

def draw_screen(misses, answer):
  clear_screen()
  formatted_answer = f" ({misses}/{MAX_MISSES}) [{' '.join(map(format_letter, answer))}] "
  print(formatted_answer.center(40, '-'))

def clear_screen():
  print("\033[H\033[J", end="")

def create_blank_answer(word):
  answer = []
  for i in range(0, len(word)):
    if word[i] == " ":
      answer.append(" ")
    else:
      answer.append(None)
  return answer

def format_letter(letter):
  if letter is None:
    return "_"
  else:
    return letter.upper()
  
main()