# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import simplegui
import random

# convert the player's choice to player_number using the function name_to_number()
def name_to_number(name):
    # delete the following pass statement and fill in your code below
  
    if name == "Rock":
        y = 0
    elif name == "Spock":
                y = 1
    elif name == "Paper":
                        y = 2
    elif name == "Lizard":
                                y = 3
    else:
                                        y = 4
    return y
  
  


    # convert comp_number to comp_choice using the function number_to_name()
def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        z = "Rock"
    elif number == 1:
            z = "Spock"
    elif number == 2:
                z = "Paper"
    elif number == 3:
                    z = "Lizard"
    else:
                        z = "Scissors"
    return z
                    
             
    
    
    # convert number to a name using if/elif/else


def input_handler(x):
    inp.set_text(x)
    
def transfer_Rock():
    input_handler("Rock")
    rpsls("Rock")

def transfer_Paper(): 
    input_handler("Paper")
    rpsls("Paper")    

def transfer_Spock():
    input_handler("Spock")
    rpsls("Spock")   
    
def transfer_Lizard():  
    input_handler("Lizard")
    rpsls("Lizard")
    
def transfer_Scissors():   
    input_handler("Scissors")
    rpsls("Scissors")




def rpsls(player_choice): 
   
  # print out the message for the player's choice   
    print ""
    print "Player chooses", player_choice
    pc = name_to_number(player_choice)
    
  # compute random guess for comp_number using random.randrange()
    cc = random.randrange(0,5)
    x = number_to_name(cc)
    
  # print out the message for computer's choice
    print "Computer chooses",  x
    
    if cc == pc:
        print "Player ties Computer"
    elif pc<cc<=pc+2:
            print "Computer wins!"
    elif pc>cc>=pc-2:
                    print "Player wins!"
    elif pc>cc<=pc-2:
                            print "Computer wins!"
    else:
                                    print "Player wins!" 



frame = simplegui.create_frame("RPSLS",200,200)

frame.add_button("Rock",transfer_Rock,100)
frame.add_button("Spock",transfer_Spock,100)
frame.add_button("Paper",transfer_Paper,100)
frame.add_button("Lizard",transfer_Lizard,100)
frame.add_button("Scissors",transfer_Scissors,100)


inp = frame.add_input("Which_one", input_handler, 200)



frame.start()





