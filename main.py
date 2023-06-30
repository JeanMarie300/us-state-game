import turtle
import pandas

screen = turtle.Screen()

screen.tracer(0)

screen.title("U.S States Game")

image = "blank_states_img.gif"

turtle.addshape(image)

turtle.shape(image)

stateData = pandas.read_csv("50_states.csv")

stateList = stateData['state'].to_list()

guessedStates = []
score = 0
attempt = 0

while score < 50 :
    screen.update()

    if attempt == 0 :
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")

    answer = answer_state.title()
    state = stateData[stateData["state"] == answer].state
    xCoordinate = stateData[stateData["state"] == answer].x
    yCoordinate = stateData[stateData["state"] == answer].y

    if answer == "Exit":
        stateToLearn = []
        for state in stateList:
            if state not in guessedStates:
                stateToLearn.append(state)
        df = pandas.DataFrame(stateToLearn)
        df.to_csv("states_to_learn.csv")
        break

    if not state.empty:
        turtle.penup()
        turtle.setposition(xCoordinate.item(), yCoordinate.item())
        turtle.pendown()
        turtle.write(state.item(), align="left")
        if state.item() not in guessedStates :
            guessedStates.append(state.item())
            score += 1

    turtle.penup()
    turtle.setposition(0,0)
    attempt += 1

