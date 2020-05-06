def main():
  import random #biblioteca funciones random
  
  dice_sum = 0 #variable suma de dados
  dice_rolls = 2 #variable dos dados
  
  for i in range (0,dice_rolls):
    roll = random.randint(1,6) #asigna numero random a dado
    dice_sum += roll #operacion de suma de valores de dados (dice_sum = dice_sum + roll)
    if roll == 1:
        print(f'You rolled a {roll}! Critical Fail')#imprime resultado Critical 1*
    elif roll == 6:
        print(f'You rolled a {roll}! Critical Success')#imprime resultado Critical 6*
    else:
        print(f'You rolled a {roll}')#imprime resultado dados individualmente
  print(f'You have rolled a total of {dice_sum}') #imprime la suma de los dados

if __name__== "__main__":
  main()
