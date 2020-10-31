# The program has two classes, a class mastermind which has all the required fucntions
# For the game to operate, the class game has the operating structure for the 3 variations 
# of the game. 

#the required library files
#please pip install collections before running the program
import random
from collections import Counter
import getpass

#This list holds all the available colours
colours = ['R', 'L', 'Y', 'G', 'W', 'B'] 

#class containing the player info and the fucntions for the various tasks in the game
class mastermind:

    p = [None]*4 #Player info list

    def get_players(self):
        for i in range(self):
            mastermind.p[i]= input("Player", i, ": What is your name? \n>")
        
    def code_generator(self):
        i = 0
        gen_code = ""
        while i < self:
            colour = random.randint(0, 6)
            gen_code += colours[colour]
            i = i+1
        return gen_code


    def compare(self, guess):
        blacks_count = 0
        whites_count = 0
        self_not_black = []
        other_not_black = []

        for i, peg in enumerate(self):
            if peg == guess[i]:
                blacks_count += 1
            else:
                self_not_black.append(peg)
                other_not_black.append(guess[i])

        self_not_black_counter = Counter(self_not_black)
        other_not_black_counter = Counter(other_not_black)

        for color, count in self_not_black_counter.items():
            whites_count += min(count, other_not_black_counter[color])

        out = mastermind.feedback(blacks_count, whites_count)
        return out


    def feedback(self, wc):
        out = []
        for i in range(self):
            out.append('B')
        for i in range(wc):
            out.append('W')
        if(len(out) >= 1):
            return(out)
        else:
            return ("Nothing")


    def play(self):

        print("Welcome to Mastermind!")
        print("Developed by *Your Name*")
        print("COMP 1046 Object_Oriented Programming")

        print("Select which game you want to play:")
        print("(A) Original Mastermind for 2 players")
        print("(B) Original Mastermind for 1 player")
        print("(C) Mastermind44 for 4 players")
        print("****Enter A, B, or C to continue****")
        choice = input(">")
        if(choice == 'A' or 'a'):
            mastermind.get_players(2)
            game.mastermind2(mastermind.p[0], mastermind.p[1])
        elif(choice == 'B' or 'b'):
            mastermind.get_players(1)
            game.mastermind1(mastermind.p[0])
        elif(choice == 'C' or 'c'):
            mastermind.get_players(4)
            game.mastermind44(mastermind.p[0], mastermind.p[1], mastermind.p[2], mastermind.p[3])
        else:
            print("Invalid input!")
            print("Redirecting to main menu....")
            mastermind.play(1)


    def get_code(self):
        colour_code = []
        position_code = []
        if(self == 4):
            temp1 = getpass.getpass('Enter your combination:')
            temp2 = getpass.getpass('Enter your combination again:')
            if(len(temp1) == self):
                if(temp1 == temp2):
                    soln_code = temp1
                else:
                    print(
                        "The code doesn't match the one previously entered.\n Please enter the same code twice!")
                    mastermind.get_code(self)
            else:
                print("The code entered isn't long enough. Enter again!")
                mastermind.get_code(self)
            return(soln_code)
        if(self == 5):
            temp1, temp2 = [], []
            pos = [1, 2, 3, 4, 5]
            for i in range(4):
                temp1 = getpass.getpass("Enter your code colour")
                colour_code.append(temp1)
                getpass.getpass("Enter your code colour")
                temp2 = getpass.getpass("Enter your code position, The available postions are ", pos)
                pos.pop(temp2-1)
                position_code.append(temp2)
            position_code.append(pos)
            colour_code.insert(pos-1, 'Blank')
            return (colour_code, position_code)
        
    def question(self):
        print("Do you wanna (p)lay?")
        print("Do you wanna (Q)uit?")
        out = input(">")
        return out

class game(mastermind):
    def mastermind2(self, player2):
        l = 4

        print("Welcome", self , " you need to create a code that consists of four pegs."
            " Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite,or (B)lack."
            " Specify the code by specifying four characters where each character indicates a colour as above."
            " For example, WWRG represents the code White-White-Red-Green. You need to enter the code twice."
            " No character is shown on the screen so Supermind cannot see it.")

        soln_code = mastermind.get_code(l)

        print("Welcome to Supermind", player2, "You can now start to play by guessing the code. \n"
            "Enter a guess by providing four characters and press Enter.")
        for i in range(1, 13):
            print("Attempt #", i, ":")
            guess = input(">")
            if len(guess) == 4:
                feedback = mastermind.compare(guess, soln_code)
                if(feedback == "Match"):
                    print("Congratulations! You broke the code in", i, "attempts!")
                    choice = mastermind.question(1)
                    if choice == "p" or "P":
                        mastermind.play(1)
                    else:
                        print("Goodbye!")
                        exit()
            else:
                print("This attempt is incorrect. You must provide exactly four characters and"
                    "they can only be, R, L, G, Y, W or B.")
            print("Feedback on attempt #", i, ":", feedback)


    def mastermind1(self):
        l = 4

        print("Welcome,", self , "You have to guess the code generated by the computer"
            "The code cponsists of 4 pegs Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, "
            "(W)hite,or (B)lack. Specify the code by specifying four characters where each"
            "character indicates a colour as above. For example, WWRG represents the code White-White-Red-Green.")

        soln_code = mastermind.code_generator(4)
        for i in range(1, 13):
            print("Attempt #", i, ":")
            guess = input(">")
            if len(guess) == l:
                feedback = mastermind.compare(guess, soln_code)
                if(feedback == "Match"):
                    print("Congratulations! You broke the code in", i, "attempts!")
                    choice = mastermind.question(1)
                    if choice == "p" or "P":
                        mastermind.play(1)
                    elif choice == 'q' or 'Q':
                        print("Goodbye!")
                        exit()
                    else:
                        print("Invalid input! Quitting..")
                        exit()
            else:
                print("This attempt is incorrect. You must provide exactly four characters and"
                    "they can only be, R, L, G, Y, W or B.")
            print("Feedback on attempt #", i, ":", feedback)


    def mastermind44(self, player2, player3, player4):
        l = 5

        soln_colour, soln_position = mastermind.get_code(l)
        soln_code = [None]*5
        a = 0
        for i in soln_position:
            soln_code[i-1] = soln_colour[a]
            a += 1

        for i in range(1, 6):
            for j in range(0, l):
                print("Player #", j, "Enter your guess: ")
                guess = input(">")
                feedback = mastermind.compare(guess, soln_code)
                if len(guess) == 5:
                    feedback = mastermind.compare(guess, soln_code)
                    if(feedback == "Match"):
                        print("Congratulations! You broke the code in", i, "attempts!")
                        choice = mastermind.question(1)
                        if choice == "p" or "P":
                            mastermind.play(1)
                        elif choice == 'q' or 'Q':
                            print("Goodbye!")
                            exit()
                        else:
                            print("Invalid input! Quitting..")
                            exit()
                else:
                    print("This attempt is incorrect. You must provide exactly four characters and"
                        "they can only be, R, L, G, Y, W or B.")
                print("Feedback on attempt #", i, ":", feedback)
