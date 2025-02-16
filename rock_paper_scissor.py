import random
score=0
game_over=False
while not game_over:
    user_choice=input("enter your choice:  '0' for rock,'1' for paper,'2' for scissor, 'x' to exit game: ")
    if user_choice.lower()=="x":
        print("exit game,thank you🙌")
        break 
    if user_choice.isdigit():
        user_choice=int(user_choice)
        if user_choice not in [0,1,2]:
            print("invalid choice😒")
            continue
    else:
        print("invalid choice ,please enter valid choice 😞")
        continue
    choices=["✊","✋","✌️"]
    print(f"your choice:{choices[user_choice]}")
    computer_choice=random.randint(0,2)
    print(f"computer choice:{choices[computer_choice]}")
    if user_choice==computer_choice:
        print("It's a draw")
    elif (user_choice==0 and computer_choice==2) or (user_choice==2 and computer_choice==1) or (user_choice==1 and computer_choice==0):
        score+=1
        print(f"you win with score {score}😍")
    else:
        print("you lose!😭")