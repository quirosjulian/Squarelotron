# Squarelotrons
# By Julian Quiros

import copy

def make_squarelotron(list):
    """Given a flat list of 25 numbers, make and return a squarelotron. Represent as
a list of lists"""

    squarelotron = []
    squarelotron = [
        list[0:5],
        list[5:10],
        list[10:15],
        list[15:20],
        list[20:25] ]
    return squarelotron

def make_list(squarelotron):
    """Inverse of make_squarelotron, returns a list of 25 numbers"""

    flat_list = []
    for row in squarelotron:
        flat_list = flat_list + row
    return flat_list

def swap_numbers(squarelotron, index1, index2):
    """Takes the number at location index1, and swap with number at index2"""
    new_squarelotron = make_list(squarelotron)
    a = new_squarelotron[index1]
    new_squarelotron[index1] = new_squarelotron[index2]
    new_squarelotron[index2] = a
    cum_squarelotron = make_squarelotron(new_squarelotron)
    return cum_squarelotron

def upside_down_flip(squarelotron, ring):
    """Performs the Upside-Down flip of the squarelotron, and returns the new
    squarelotron. Original squarelotron should not be modified."""

    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == "inner":
        new_squarelotron = swap_numbers(new_squarelotron, 6, 16)
        new_squarelotron = swap_numbers(new_squarelotron, 7, 17)
        new_squarelotron = swap_numbers(new_squarelotron, 8, 18)
    elif ring == "outer":
        new_squarelotron = swap_numbers(new_squarelotron, 0, 20)
        new_squarelotron = swap_numbers(new_squarelotron, 1, 21)
        new_squarelotron = swap_numbers(new_squarelotron, 2, 22)
        new_squarelotron = swap_numbers(new_squarelotron, 3, 23)
        new_squarelotron = swap_numbers(new_squarelotron, 4, 24)
        new_squarelotron = swap_numbers(new_squarelotron, 5, 15)
        new_squarelotron = swap_numbers(new_squarelotron, 9, 19)
    return new_squarelotron
        

    
def left_right_flip(squarelotron, ring):
    """Performs the Left-Right flip of the squarelotron. Returns the new squarelotron
    Original not modified."""

    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == "inner":
        new_squarelotron = swap_numbers(new_squarelotron, 6, 8)
        new_squarelotron = swap_numbers(new_squarelotron, 11, 13)
        new_squarelotron = swap_numbers(new_squarelotron, 16, 18)
    if ring == "outer":
        new_squarelotron = swap_numbers(new_squarelotron, 0, 4)
        new_squarelotron = swap_numbers(new_squarelotron, 1, 3)
        new_squarelotron = swap_numbers(new_squarelotron, 5, 9)
        new_squarelotron = swap_numbers(new_squarelotron, 10, 14)
        new_squarelotron = swap_numbers(new_squarelotron, 15, 19)
        new_squarelotron = swap_numbers(new_squarelotron, 20, 24)
        new_squarelotron = swap_numbers(new_squarelotron, 21, 23)
    return new_squarelotron

def inverse_diagonal_flip(squarelotron, ring):
    """Performs the Main Inverse Diagonal of the squarelotron. Returns new, Original
    not modified."""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == "inner":
        new_squarelotron = swap_numbers(new_squarelotron, 6, 18)
        new_squarelotron = swap_numbers(new_squarelotron, 7, 13)
        new_squarelotron = swap_numbers(new_squarelotron, 11, 17)
    if ring == "outer":
        new_squarelotron = swap_numbers(new_squarelotron, 0, 24)
        new_squarelotron = swap_numbers(new_squarelotron, 1, 19)
        new_squarelotron = swap_numbers(new_squarelotron, 2, 14)
        new_squarelotron = swap_numbers(new_squarelotron, 3, 9)
        new_squarelotron = swap_numbers(new_squarelotron, 5, 23)
        new_squarelotron = swap_numbers(new_squarelotron, 10, 22)
        new_squarelotron = swap_numbers(new_squarelotron, 15, 21)
    return new_squarelotron

def main_diagonal_flip(squarelotron, ring):
    """Performs the Main Diagonal Flip of the squarelotron, Returns new, Original
    not modified."""
    new_squarelotron = copy.deepcopy(squarelotron)
    if ring == "inner":
        new_squarelotron = swap_numbers(new_squarelotron, 7, 11)
        new_squarelotron = swap_numbers(new_squarelotron, 8, 16)
        new_squarelotron = swap_numbers(new_squarelotron, 13, 17)
    if ring == "outer":
        new_squarelotron = swap_numbers(new_squarelotron, 1, 5)
        new_squarelotron = swap_numbers(new_squarelotron, 2, 10)
        new_squarelotron = swap_numbers(new_squarelotron, 3, 15)
        new_squarelotron = swap_numbers(new_squarelotron, 4, 20)
        new_squarelotron = swap_numbers(new_squarelotron, 9, 21)
        new_squarelotron = swap_numbers(new_squarelotron, 14, 22)
        new_squarelotron = swap_numbers(new_squarelotron, 19, 23)
    return new_squarelotron

def welcome_statement():
    print("""Welcome to Squarelotron!\nYou may move the board in 4 directions.
Either Upside Down, Left to Right, by the Main diagonal, or by the Inverse Diagonal.
When prompted, enter either "upside down", "left to right", "main", or "inverse" to do so.
These movements are performed on either the Outer or Inner ring, which is of your choosing by entering "outer" or "inner".
Your moves are cumulative, and you may elect to have a new board during any turn.""")
          


def play_again():
    """Ask if User wants to play again, and if they want a new board. If no
    then game ends"""
    play_again = input("Would you like to move the squarelotron (y or n)?:")
    while play_again != "Y" and play_again != "y" and play_again != "N" and play_again != "n":
        play_again = input("Please give a valid input:")
    if play_again == "Y" or play_again == "y":
        user_input()
    if play_again == "N" or play_again == "n":
        print("Thanks for playing.")
        
 


def user_input():
    """Loop where user inputs which ring and direction they want to move,
    and if they want to quit or want a new board."""
    list = []
    for i in range(1,26):
        list.append(i)
    squarelotron = make_squarelotron(list)
    original = copy.deepcopy(squarelotron)
    new_squarelotron = []
    new_board = "N"
    while True:
        if new_board == "Y" or new_board == "y":
            squarelotron = original
            for i in range (0,5):
                print(squarelotron[i])
    
        ring = input("Which ring would you like to rotate?:")
        while ring != "inner" and ring != "Inner" and ring != "Outer" and ring!= "outer":
            ring = input("Please give a valid input:")
        if ring == "Outer" or ring == "outer":
            direction = input("In which direction would you like to rotate the ring?:")
            while direction != "upside down" and direction != "left to right" and direction != "main" and direction != "inverse":
                direction = input("Please give a valid input:")
            if direction == "upside down":
                new_squarelotron = upside_down_flip(squarelotron, ring)
            if direction == "left to right":
                new_squarelotron = left_right_flip(squarelotron, ring)
            if direction == "main":
                new_squarelotron = main_diagonal_flip(squarelotron, ring)
            elif direction == "inverse":
                new_squarelotron = inverse_diagonal_flip(squarelotron, ring)
            

        elif ring == "Inner" or ring == "inner":
            direction = input("In which direction would you like to rotate the ring?:")
            while direction != "upside down" and direction != "left to right" and direction != "main" and direction != "inverse":
                direction = input("Please give a valid input:")
            if direction == "upside down":
                new_squarelotron = upside_down_flip(squarelotron, ring)
            if direction == "left to right":
                new_squarelotron = left_right_flip(squarelotron, ring)
            if direction == "main":
                new_squarelotron = main_diagonal_flip(squarelotron, ring)
            elif direction == "inverse":
                new_squarelotron = inverse_diagonal_flip(squarelotron, ring)
            

        else:
            ring = input("Which ring would you like to rotate?:")
        squarelotron = new_squarelotron
        for i in range (0,5):
            print(squarelotron[i])
        end_game = input("Would you like to quit (y or n)?:")
        while end_game != "N" and end_game != "n" and end_game != "Y" and end_game != "y":
            end_game = input("Please give a valid input:")
        if end_game == "N" or end_game == "N":
            user_input()
        elif end_game == "Y" or end_game == "y":
            print("Thanks for playing.")
            break
        new_board = input("Would you like a new board (y or n)?:")
    

        
    
            

def print_squarelotron():
    squarelotron = ([[1, 2, 3, 4, 5],
                         [6, 7, 8, 9, 10],
                         [11, 12, 13, 14, 15],
                         [16, 17, 18, 19, 20],
                         [21, 22, 23, 24, 25]])
    for i in range (0,5):
        print(squarelotron[i])
    


def main():
    welcome_statement()
    print_squarelotron()
    play_again()



if __name__ == "__main__":
        main()











        

