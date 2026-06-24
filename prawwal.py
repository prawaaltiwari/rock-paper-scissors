import random 
choices = ['rock', 'paper', 'scissors']
print("welcome to lunch time game")
while True:     
    unc = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
    if unc in ['exit', 'quit','q','e']:
        print("thank you for playing!")
        break

    if unc not in choices:
        print("invalid choice. try again.")
        continue
    
    cuc = random.choice(choices)
    print(f"computer chose:-{cuc}")
    if unc == cuc:
        print("its a tie!")
    elif ('rock' == unc and 'scissors' == cuc) or (unc == 'paper' and cuc == 'rock') or (unc == 'scissors' and cuc == 'paper'):
         print("you win!")
    else :
         print("you lose ")
    play_again = input("do you want to play again? (yes/no): ").lower()
    if play_again not in ['yes','y']:
        print('thank you for playing!')
        break
    
