from random import choice
from replit import clear

def check_answer(a_folower_count, b_folower_count, guess):
  if a_folower_count > b_folower_count:
    return guess == 'a'
  else:
    return guess == 'b'
    
data = [{'name': 'Instagram', 
     'follower_count': 345},
    {'name': 'Cristiano Ronaldo', 
     'follower_count': 215},
    {'name': 'Ariana Grande', 
     'follower_count': 183}]

score = 0 
while True:
  A = choice(data)
  B = choice(data)
  if A == B:
    B = choice(data)
  a_folower_count = A["follower_count"]
  b_folower_count = B["follower_count"]    
  guess = input(f'Compare A:{A["name"]}\nAganist B::{B["name"]}\nWho has more followers a or b: ')
  if check_answer(a_folower_count, b_folower_count, guess) == True:
    clear()
    score += 1
    print(f'Youre right Current score {score}')
  else:
    print(f'Sorry, thats wrong. Final score: {score}')
    break
  

