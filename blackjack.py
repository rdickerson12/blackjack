import random

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
play_again = 'yes'
while play_again == 'yes':
  sum = random.choice(card_values)
  print(f"Your first card was {sum}")
  turn = "hit"

  while turn == "hit":
    card_value = random.choice(card_values)
    print(f"Your next card was {card_value}")
    #sum = sum + card_value is another way to put it
    sum += random.choice(card_values)
    print("You currently have: " + str(sum))
    if sum < 21:
      turn = input("What do you want to do? ")
    else: 
      turn = 'stop'

  if sum > 21:
    print("You went over 21!")
  elif sum == 21:
    print ("You win!")
  else:
    print("You stopped at: " + str(sum))

    play_again = input("Want to play again?")