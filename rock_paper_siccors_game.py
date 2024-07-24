import random
import time 

#instructions
print('''Well come to Rock,paper and scissor!!!
      ---> 1.ROCK, 2.PAPER, 3.SCISSOR <---

      ''')
time.sleep(1)
print('''Rules:
      ROCK > SCISSOR
      SCISSOR> PAPER
      PAPER > ROCK

      ''')
time.sleep(1)

print("Lets Start the game !!!")
time.sleep(1)
# Opions
opts={
    1: "ROCK",
    2: "PAPER",
    3: "SCISSOR"
}

# a condition loop for taking inputs from user
while True:
    try:
        user_choice= int(input("Please enter your Chioce between 1,2,3:  "))
    except:
        # for entering invalid entrys like non_integers
        print("Warning !!!.  invalid entry")
        time.sleep(1)
        # checking for user entry is valid or not
    if user_choice not in [1,2,3]:
        print("Sorry!. You have entered Invalid option. Please Choose carefully.")
        time.sleep(1)
    else:
        winner= False

        # computer choice to choose
        comp_chocie= random.randint(1,3)

        print(f'Your chocie : {opts[user_choice]}\nComputer Choice : {opts[comp_chocie]}')

        time.sleep(2)
        # Delclaring the result By checking all posibilities of user's win. else computers win
        if comp_chocie==user_choice:
            print("Both choose same Its a Draw. lets start again")
        elif comp_chocie==1 and user_choice==2:
            print("You Won the match.!!! Congartualations")
            winner=True
        elif comp_chocie==2 and user_choice==3:
            print("You Won the match.!!! Congartualations")
            winner=True
        elif comp_chocie==3 and user_choice==1:
            print("You Won the match.!!! Congartualations")
            winner=True
        else:
            print(" Sorry !!!. You Lost the game")
        time.sleep(1)
        # asking for continue or exit the game
        if winner:
            ch=input("Do You want to Continue the game\nY/N")
            if ch=="Y" or ch=="y":
                pass
            else:
                break
        else:
            ch=input("Do You want to Re-play the game\nY/N")
            if ch=="Y" or ch=="y":
                pass
            else:
                break
time.sleep(1)
print("The Game has terminated")
    



    

