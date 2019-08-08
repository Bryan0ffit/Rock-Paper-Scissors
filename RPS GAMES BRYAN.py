import random


user_r = 0
user_p = 0
user_s = 0

user_wins = 0
comp_wins = 0
ties = 0

status = True

while status:

    if user_r > user_p and user_s:
        x = 2
    if user_p > user_r and user_s:
        x = 3
    if user_s > user_p and user_r:
        x = 1
    if user_s == user_p == user_r:
        x = random.randint(1,3)


    

 #   x = random.randint(1,3)


    if x == 1:
        comp_choice = 'r'
    elif x == 2:
        comp_choice = 'p'
    elif x == 3:
        comp_choice = 's'

    print("###Round has begun###\nSelect your weapon")

    user_choice = input()

    

    if user_choice == 'r':
        user_r += 1
        print("The Computer chose: " + comp_choice)
    if user_choice == 'p':
       user_p += 1
       print("The Computer chose: " + comp_choice)
    if user_choice == 's':
       user_s += 1
       print("The Computer chose: " + comp_choice)
    if user_choice == 'q':
       status = False

       print("Computer wins: "  + str(comp_wins))
       print("User wins: " + str(user_wins))
       print("Ties: " + str(ties))
       print("Amount of times you chose rock: " +  str(user_r))
       print("Amount of times you chose paper: " + str(user_p))
       print("Amount of times you chose scissors: " + str(user_s))
        
    if comp_choice == 'r' and user_choice == 'r':
        ties += 1
        print("***No one wins***\n")
    if comp_choice == 'r' and user_choice == 'p':
        user_wins += 1
        print("***User Wins***\n")
    if comp_choice == 'r' and user_choice == 's':
        comp_wins += 1
        print("***Copmuter Wins***\n")

    if comp_choice == 'p' and user_choice == 'p':
        ties += 1
        print("***No one wins***\n")
    if comp_choice == 'p' and user_choice == 's':
        user_wins += 1
        print("***User Wins***\n")
    if comp_choice == 'p' and user_choice == 'r':
        comp_wins += 1
        print("***Copmuter Wins***\n")

    if comp_choice == 's' and user_choice == 's':
        ties += 1
        print("***No one wins***\n")
    if comp_choice == 's' and user_choice == 'r':
        user_wins += 1
        print("***User Wins***\n")
    if comp_choice == 's' and user_choice == 'p':
        comp_wins += 1
        print("***Copmuter Wins***\n")


    
""" use if statements to set total number of r,p, or s chosen"""
