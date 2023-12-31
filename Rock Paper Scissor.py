import random
user_name = input("Enter your name: ")
print(f"Welcome {user_name}! Let's play the game\n")
print('''Here are some rules before we start the game:
1.Rock wins against scissor 
2.Paper wins against rock 
3.Scissor wins against paper\n''')
print(">>> Enter 'exit' to close the game\n")

choice_list = ["rock", "paper", "scissor"]
while True:
    user_choice = input("Enter your choice (rock,paper,scissor,exit): ")
    comp_choice = random.choice(choice_list)
    if user_choice == "exit":
        print("GAME ENDED ! Thanks for playing " + user_name)
        break
    else:
        print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("Both chooses same: = Match Tie")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("paper covers rock = Computer won")
        else:
            print("rock smashes scissor = You won " )

    elif user_choice == "paper":
        if comp_choice == "scissor":
            print("scissor cuts paper, Computer won")
        else:
            print("paper covers rock,You won " )

    elif user_choice == "scissor":
        if comp_choice == "paper":
            print("scissor cuts paper, You won " )
        else:
            print("rock smashes scissor, Computer won")
    else:
        print ("Invalid input,try again!")
    




    
        
            
