# The program has two classes, a class mastermind which has all the required fucntions #
# For the game to operate, the class game has the operating structure for the 3 variations #
# of the game. #

#the required library files#
#please pip install collections before running the program@
import random
from collections import Counter
import getpass

#This list holds all the available colours
colours = ['R', 'L', 'Y', 'G', 'W', 'B'] 




class code:
    '''This class contains the function code_generator to generate code for the single player game
        and the fucntion get_code is used to get input from the user either for the 2 player por 4 player versions,
        The input provided in this fucntion is used as the secret code'''
    # to generate code in the single player game
    def code_generator(self, l):
        i = 0
        gen_code = ""
        # code generating algorithm using random
        while i < l:
            colour = random.randint(0, 6)
            gen_code += colours[colour]
            i = i+1
        return gen_code

    
    # to get the code from the player according to the kind of game
    def get_code(self, l):
        colour_code = []
        position_code = []
        self.l = l
        # 2 player version
        if(self.l == 4):
            temp1 = getpass.getpass('Enter your combination:')
            temp2 = getpass.getpass('Enter your combination again:')
            if(len(temp1) == self.l):
                if(temp1 == temp2):
                    soln_code = temp1
                else:
                    print("The code doesn't match the one previously entered.\n Please enter the same code twice!")
                    return 'X'
                    
            else:
                print("The code entered isn't long enough. Enter again!")
                code_1 = code()
                code_1.get_code(l)
            return(soln_code)
            
        # 4 player version
        if(self.l == 5):
            pos = ['1', '2','3', '4', '5']
            i=4
            while i>0:
                temp1 = input("Enter your code colour: ")
                colour_code.append(temp1)
                print("Available positions are:", pos)
                temp2 = input("Enter your code position ")
                pos.remove(temp2)
                position_code.append(temp2)
                i-=1
            position_code.append(pos)
            colour_code.insert(((int(pos[0])-1)), 'X')
            return (colour_code, position_code)


    def check_code(self, code):
        flag = 0
        if(set(code).issubset(set(colours))): 
            flag = 1
        return flag


                    
    
class compare_code:
    ''' This class contains the code to compare the secret and the correct code '''

    # To compare the guess made by a player and the solution code 
    # and returning the number of blacks and whites accordingly
    def compare(self, code, guess):
        if guess == code:
            return "Match"
        else:
            blacks_count = 0
            whites_count = 0
            self_not_black = []
            other_not_black = []

            #matching and finding the correct positions and colour
            for i, peg in enumerate(code):
                if peg == guess[i]:
                    blacks_count += 1
                else:
                    self_not_black.append(peg)
                    other_not_black.append(guess[i])

            self_not_black_counter = Counter(self_not_black)
            other_not_black_counter = Counter(other_not_black)

            for color, count in self_not_black_counter.items():
                whites_count += min(count, other_not_black_counter[color])

            # making the list of blacks and whites    
            out = []
            while blacks_count>0:
                out.append('B')
                blacks_count -=1
            while whites_count>0:
                out.append('W')
                whites_count -=1
            if(len(out) >= 1):
                return(out)
            else:
                return ("Nothing")
        

        
# to get the players
class player:
    '''Contains the player info'''
    
    p = [None]*4
    def get_players(self, n):
        for i in range(n):
            print("Player ", i)
            player.p[i]= input(" What is your name? \n >")


class game:
    ''' This class contains functions mastermind1, mastermind2, mastermind44 which are the implementation of the 
        4 versions of the game, this class is completely dependent on the other classes and inherits multiple fucntions
        From the classes defined above'''

    # 2 player game
    def mastermind2(self):
        player_1 = player()
        player_1.get_players(2)
        l = 4
        print("\n\n Welcome", player_1.p[0] , "you need to create a code that consists of four pegs."
            " Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite,or (B)lack."
            " Specify the code by specifying four characters where each character indicates a colour as above."
            " For example, WWRG represents the code White-White-Red-Green. You need to enter the code twice."
            " No character is shown on the screen so Supermind cannot see it.\n\n")

        #getting code from the mastermind class
        code_1 = code()
        soln_code = code_1.get_code(l) 
        if soln_code != 'X':


            print("Welcome to Supermind", player_1.p[1], "You can now start to play by guessing the code. \n"
                "Enter a guess by providing four characters and press Enter.\n\n")
            
            # creating 12 attempts for the 2nd player to guess
            for i in range(1, 13):
                print("Attempt #", i, ":")
                guess = input(">")

                if (len(guess) == 4 and code_1.check_code(guess)):
                    compare_code_1 = compare_code()
                    feedback = compare_code_1.compare(guess, soln_code)

                    #when matched the game automatically switches to the main menu
                    if(feedback == "Match"):
                        print("Congratulations! You broke the code in", i, "attempts!")
                        break
                    
                    else:
                        print("Feedback on attempt #", i, ":", feedback)
                # in case of an invalid input
                else:
                    print("This attempt is incorrect. You must provide exactly four characters and"
                        "they can only be, R, L, G, Y, W or B.")
        else:
            soln_code = code_1.get_code(l)
            # providing feedback
            


    def mastermind1(self):
        l = 4
        player_1 = player()
        player_1.get_players(1)
        print("Welcome,", player_1.p[0] , "You have to guess the code generated by the computer"
            "The code cponsists of 4 pegs Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, "
            "(W)hite,or (B)lack. Specify the code by specifying four characters where each"
            "character indicates a colour as above. For example, WWRG represents the code White-White-Red-Green.")

        # Auto generating the code
        code_1 = code()
        soln_code = code_1.code_generator(4)

        # Giving the player 12 attempts to guess the code
        for i in range(1, 13):
            print("Attempt #", i, ":")
            guess = input(">")
            x = code_1.check_code(guess)
            if (len(guess) == l and x == True):
                compare_code_1 = compare_code()
                feedback = compare_code_1.compare(guess, soln_code)
                #automatically going to the main menu if guessed correctly
                if(feedback == "Match"):
                    print("Congratulations! You broke the code in", i, "attempts!")
                    break
                else:
                    print("Feedback on attempt #", i, ":", feedback)                
            # in case of invaid input            
            else:
                print("This attempt is incorrect. You must provide exactly four characters and"
                    "they can only be, R, L, G, Y, W or B.")
        if feedback != "Match":
            print(soln_code)

            # giving the appropriate feedback
            


    # 4 player version
    def mastermind44(self):
        l = 5
        #getting the code and creating the code accordingly
        print("There are 4 players in the game, Each player enters a colour and a position from the available slots,"
        "After all the 4 slots are filled, the remaining slot is left blank. Each player gets 5 turns, you have to guess"
        "The 5 colour code which includes the blank in the correct order. \n"
        "The blank is denoted by 'X' and the rest of the colours are (R)ed, B(L)ue, (G)reen, (Y)ellow, "
        "(W)hite,or (B)lack. Specify the code by specifying four characters where each")
        code_1 = code()
        soln_colour, soln_position = code_1.get_code(l)
        soln_code = [None]*5
        a = 0
        for i in soln_position:
            soln_code[(int(i[0])-1)] = soln_colour[a]
            a += 1
        # giving 5 rounds to each player to guess the code
        for i in range(1, 6):
            for j in range(0, l):
                print("Player #", j, "Enter your guess: ")
                guess = input(">")
                compare_code_1 = compare_code()
                if (len(guess) == 5):
                    feedback = compare_code_1.compare(guess, soln_code)
                    if(feedback == "Match"):
                        print("Congratulations! You broke the code in", i, "attempts!")
                    else:
                        print("Feedback on attempt #", i, ":", feedback)
                # In case of invalid feedback
                else:
                    print("This attempt is incorrect. You must provide exactly five characters and"
                        "they can only be, R, L, G, Y, W or B. and X")
                

class mastermind(player, code, compare_code, game):
    ''' This is the initial class to initialize the game and drive the menu'''
    out = ''
    # to ask the question whether to play or not    
    def __init__(self):
        print("Do you wanna (p)lay?")
        print("Do you wanna (Q)uit?")
        mastermind.out = input(">")

    def play(self):
        print("Welcome to Mastermind!")
        print("Developed by *Your Name*")
        print("COMP 1046 Object_Oriented Programming")

        print("Select which game you want to play:")
        print("(A) Original Mastermind for 2 players")
        print("(B) Original Mastermind for 1 player")
        print("(C) Mastermind44 for 4 players")
        print("****Enter A, B, or C to continue****")
        choice = input("\n\n >")

        return choice


m = mastermind()
c='p'
while c == 'p':
    c = m.out
    choice = m.play()
    #initializing various games depending on which one tha player wants to play
    # with their respective players
    if(choice == 'A' or choice == 'a'):
        m.mastermind2()
    elif(choice == 'B' or choice =='b'):
        m.mastermind1()
    elif(choice == 'C' or choice =='c'):
        m.mastermind44()
    else:
        print("Invalid input!")
        print("Redirecting to main menu....")




