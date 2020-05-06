def main():
  import random #biblioteca funciones random
  
  dice_sum = 0 #variable suma de dados
  dice_rolls = int(input('How many dice would you like to roll? ')) #variable cantidad de dados
  dice_size = int(input('How many sides are in the dice?) ')) #variable tamaño de cada uno de dados
  
  for i in range (0,dice_rolls):
    roll = random.randint(1,dice_size) #asigna numero random a dado
    dice_sum += roll #operacion de suma de valores de dados (dice_sum = dice_sum + roll)
    if roll == 1:
        print(f'You rolled a {roll}! Critical Fail')#imprime resultado Critical 1*
    elif roll == dice_size:
        print(f'You rolled a {roll}! Critical Success')#imprime resultado Critical 20*
    else:
        print(f'You rolled a {roll}')#imprime resultado de dados individualmente
  print(f'You have rolled a total of {dice_sum}') #imprime la suma de los dados

if __name__== "__main__":
  main()
