def choice():
    """returns choice in lowercase"""
    choice = raw_input("Enter a choice: ")
    return choice.lower()

def compare(choice1, choice2):
    """rock, paper, scissors match evaluator"""
    if choice1 == choice2:
        print("It is a tie!")
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            print('Rock wins!')
        elif choice2 == 'paper':
            print('Paper wins!')
    elif choice1 == 'paper':
        if choice2 == 'scissors':
            print('Scissors wins!')
        elif choice2 == 'rock':
            print('Paper wins!')
    elif choice1 == 'scissors':
        if choice2 == 'paper':
            print("Scissors wins!")
        elif choice2 == 'rock':
            print("Rock wins!")
    else:
        print("Something is wrong.")

rounds = int(raw_input("Enter number of rounds: "))
counter = 0
while counter != rounds:
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
    counter += 1


