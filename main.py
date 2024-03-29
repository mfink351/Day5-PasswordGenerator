#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
totalChars = nr_letters + nr_symbols + nr_numbers
pw = ""

while totalChars > 0:
  charChoice = random.randint(0,2)
  if charChoice == 0 and nr_letters > 0:
    pw += str(random.choice(letters))
    nr_letters -= 1
    totalChars -= 1
  elif charChoice == 1 and nr_symbols > 0:
    pw += str(random.choice(symbols))
    nr_symbols -= 1
    totalChars -= 1
  elif charChoice == 2 and nr_numbers > 0:
    pw += str(random.choice(numbers))
    nr_numbers -= 1
    totalChars -= 1
print(f"Your password is {pw}")