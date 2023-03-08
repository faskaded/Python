from replit import clear
from art import logo
auction = {}
print(logo)
def add_info(name, bid):
  auction[name] = bid
print('Welcome to the secret auction program')
flag = True
while flag == True:
  a = input("What is your name?: ")
  bid = int(input("Whas's your bid?: "))
  add_info(a,bid)
  flag = input("Are there any other bidders? type 'yes' or 'no': ").lower()
  if flag == 'no':
    clear()
    flag = True
  else:
    flag = False
max_val = max(auction.values())
max_bid = max(auction, key = auction.get(max_val))
print(f"The winner is {max_bid} with a bid of {max_val}$")