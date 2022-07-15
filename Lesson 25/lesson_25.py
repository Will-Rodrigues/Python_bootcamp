# Process to get x, y for every states
# def get_mouse_x_y(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_x_y)

from turtle import Screen, Turtle
import pandas

# Making the loop switch
is_on = True

# Create the canvas
screen = Screen()
screen.title("U.S. Game")
screen.bgpic("lesson 25/blank_states_img.gif")

# Calling the turtle to write the name of states
letters = Turtle()
letters.up()
letters.hideturtle()

# Calling the csv with pandas
states = pandas.read_csv("lesson 25/50_states.csv")

# Keeping track of correct answers
already_guessed = []

while is_on:
    guess = screen.textinput(f"{len(already_guessed)}/{len(states.state)}",
                             "Do you know all the states of USA?").title()

    if guess == 'Quit':
        missing_states = [state for state in states if state not in already_guessed]
        # I have made a change here, after lesson 26 and commented the code before the change
        # missing_states = []
        # for state in states.state:
            # if state not in already_guessed:
                # missing_states.append(state)
        pandas.DataFrame(missing_states).to_csv("lesson 25/states_to_learn.csv")
        break

    for state in states.state:
        if guess == state:
            if state not in already_guessed:
                actual_state = states[states.state == state]
                x = int(actual_state.x)
                y = int(actual_state.y)
                letters.goto(x, y)
                letters.write(f"{state}")
                already_guessed.append(state)

