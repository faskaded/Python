from random import choice 
from replit import clear
from art import logo

print(f'Welcome to the Number Guessing Game!\nIm thinking of number between 1 and 100.\n{logo}')

def mod(live):
  number = choice([i for i in range(1,101)])
  while live > 0:
    print(f"You have {live} attempts remaining tu guess the number")
    user = int(input("Make a guess: "))
    if user == number:
      return 'You win congrats'
      break
    print(['Too lower','Too high'][user > number], '\nGuess again.')
    live-=1
  return'You lose'

def play():
  choi = input('Choose a difficulty. Type "easy" or "hard": ')
  if choi == 'easy':
    live = 10
    print(mod(live))
  else:
    live = 5
    print(mod(live))
  repl = input('You have play again ?')
  if repl == 'y':
    clear()
    play()
  else:
    return 'bay'
    
print(play())
