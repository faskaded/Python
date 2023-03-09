from replit import clear


#Calculator

#Add

def add(n1:int, n2:int):
  return n1 + n2
  
#Subtract
  
def Subtract(n1:int, n2:int):
  return n1 - n2

#Multiplying
  
def Multiplying(n1:int, n2:int):
  return n1 * n2

#Divide
  
def Divide(n1:int, n2:int):
  return n1 / n2
  
def Calculator():
  operation = {
   "+": add,
   "-": Subtract,
   "*": Multiplying,
   "/": Divide
  }
  Hod = True
  num1 =  float(input("enter a number: ")) 
  
  while Hod:
    symbol = input("what do you want to do: ")
    num2 =  float(input("enter a number: ")) 
    func = operation[symbol]
    answer = func(num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to contionue calculating with {answer} or type 'n' to exit or e for stop") == 'y':
      num1 = answer
      clear()
    else:
      Hod = False

Calculator()
