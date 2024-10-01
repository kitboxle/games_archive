import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.") 
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")




def print_revealed_phrase(guess_phrase, user_guess):
  base = ''
  under = '_'
  for letters in guess_phrase:
    if letters in user_guess or letters.isalpha()==False:
      base+= letters
    else:
      base+= under
  print(base)

#works


def get_letter(already_guessed):
  while True:
    letter = input("Please enter a letter: ")
    if not letter.isalpha():
      print(f'"{letter}" is not a letter!')
      continue
    if letter.upper() in already_guessed:
      print(f'"{letter.upper()}" has already been guessed!')
      continue
    if len(letter) != 1:
      print(f'"{letter}" is not a letter!')
    else:
      x = letter.upper()
      break
  return x


#works

def won(answered, guessed):
  box = []
  count_g = 0
  z = sorted(guessed)
  for letters in answered:
    if letters.isalpha():
      if letters not in box:
        box.append(letters)
        y = sorted(box)
  let_a = len(box)
  for stuff in guessed:
    if stuff in box:
      count_g +=1
    else:
      continue
  if let_a == count_g:
    return True
  else:
    return False
  
#works

def play_game():
  misses = 0  #start
  guesses = []
  answer = make_phrase()
  print('*** Welcome to Hangman ***')
  print_gallows(misses)
  print_revealed_phrase(answer, guesses)
  print(f"Letters guessed: {guesses}")
  guess1 = get_letter(guesses)
  while True:
    y = sorted(guesses)
    if guess1 not in answer:
      misses +=1
      if misses == 6:
          print_gallows(misses)
          print('Game Over!')
          print('Solution was:', answer)
          break
      else:
          guesses.append(guess1)
          print_gallows(misses)
          print()
          print_revealed_phrase(answer, guesses)
          print(f"Letters guessed: {sorted(guesses)}")
          guess1 = get_letter(guesses)
          continue
    if guess1 in answer:
      guesses.append(guess1)
      y = sorted(guesses)
      if won(answer, y) == True:
        print()
        print(answer)
        print('Congratulations!')
        break
      else:
        print()
        print_revealed_phrase(answer, guesses)
        print(f"Letters guessed: {sorted(guesses)}")
        guess1 = get_letter(guesses)
        continue


#done

print(play_game())



