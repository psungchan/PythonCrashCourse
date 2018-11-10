import random
# Define a set of variables to hold the valid moves
rock     = "Rock"
paper    = "Paper"
scissors = "Scissors"
# default number of rounds
NUM_OF_RESPONSES = 3

# Now store the moves in a list
moves = [rock, paper, scissors]
# A dictionary of each move and what it beats
winmoves = {rock:scissors, paper:rock, scissors:paper}


def findwinner(playermove, computermove):
    if playermove == computermove:
        return "Draw!"
    # Find the player move, which will show us what that move beats
    # If the computer move is in that list, players wins, otherwise player loses    
    elif computermove in winmoves[playermove]:        
        return "Player wins!"
    
    return "Computer wins!"

def main():
    user_input = input("Enter the number of rounds you want to play: ")
    play_times = NUM_OF_RESPONSES # setting the play_times to default
    if user_input.isdigit() and int(user_input) < 100:
        # if the input was appropriate, override play_times
        play_times = int(user_input)
    else:
        # otherwise the play_times remains default
        print("Bad input. You will play", NUM_OF_RESPONSES, "times as default.")
    
    while play_times > 0:
        playermove = input("Enter your choice: "+", ".join(moves)+": ")
        computermove = random.choice(moves)
        while playermove not in moves:
            playermove = input("Bad input. Enter your choice: "+", ".join(moves)+": ")
        print(findwinner(playermove,computermove))
        play_times -= 1
            
    print ("Thanks for playing.")

main()            




