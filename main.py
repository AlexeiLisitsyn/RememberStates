import pandas
import turtle

image_map = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []
states_to_remember = []

screen = turtle.Screen()
screen.title("U.S.States Game")
screen.addshape(image_map)
turtle.shape(image_map)

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 guessed states.",
                             prompt="Can you name the US states??").title()
    if guess == "Exit":
        for state in states_list:
            if state not in guessed_states:
                states_to_remember.append(state)
            remember_table = pandas.DataFrame(states_to_remember)
            remember_table.to_csv("State's spreadsheet to remember.csv")
        break
    if guess in states_list:
        if guess in guessed_states:
            pass
        else:
            guessed_states.append(guess)
        state_cor = data[data.state == guess]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(int(state_cor.x), int(state_cor.y))
        state_turtle.write(f"{guess}")
    else:
        continue
screen.exitonclick()
