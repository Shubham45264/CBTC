import random
def secret_list(max_range):
    secret_list =[]
    for i in range(4):
      secret_list.append(random.randint(1,max_range))
    return secret_list


mastermind_list = secret_list(5)
print(mastermind_list)
print("Welcome to the Mastermind Game!")
print("Try to guess the four secret numbers.\n")

correct = 0
tries = 0
while correct < 4:
  guess1 = int(input("Please guess the first number:"))
  guess2 = int(input("Please guess the second number:"))
  guess3 = int(input("Please guess the Third number:"))
  guess4 = int(input("Please guess the fourth number:"))
  tries += 1
  
  if guess1 == mastermind_list[0]:
    correct +=1
  if guess2 == mastermind_list[1]:
    correct +=1  
  if guess3 == mastermind_list[2]:
    correct +=1
  if guess4 == mastermind_list[3]:
    correct +=1
    
  if correct < 4:
    print("You guessed" + str(correct) + "number(s) correctly.")
    correct = 0
    Continue 
  else:
    if tries == 1:
      print("Congratulations, You guessed all four numbers correctly!")
      print("It took you" + str(tries) + "\ttries.")
    else:
      print("Congratulations, You guessed all four numbers correctly!")
  
     




  
  