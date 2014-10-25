import random
import simplegui

secret_number=0
num_range=100
num_of_guesses=0

# helper function to start and restart the game
def new_game():
    global num_of_guesses
    global num_range
    global secret_number
    if(num_range==100):
        num_of_guesses=7
        print "New Game. Range is from 0 to", num_range
        print "Number of remaining guesses is", num_of_guesses
        print ""
    elif(num_range==1000):
        num_range=1000
        print "New Game. Range is from 0 to", num_range
        num_of_guesses=10
        print "Number of remaining guesses is", num_of_guesses
        print ""
    secret_number=random.randrange(0,num_range)


# define event handlers for control panel
def range100():
    global num_range
    num_range=100
    print ""
    new_game()

def range1000():
    global num_range
    num_range=1000
    print ""
    new_game()


def input_guess(guess):
    print "Guess was", int(guess)
    global num_of_guesses
    global num_range
    if(num_of_guesses>0):
        num_of_guesses=num_of_guesses-1
        print "Number of remaining guesses is", num_of_guesses
        if(int(guess)>secret_number):
            print "Higher"
        elif(int(guess)<secret_number):
            print "Lower"
        elif(int(guess)==secret_number):
            print "Correct"
            print ""
            num_range=100
            new_game()
        print ""
    else:
        print "Out of choices."
        print ""
        num_range=100
        new_game()


# create frame
f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a Guess" , input_guess, 200)

# register event handlers for control elements and start frame


# call new_game 
new_game()        

