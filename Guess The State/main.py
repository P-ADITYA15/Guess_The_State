'''Importing the Dependencies'''
import turtle
import pandas

'''Reading Csv file'''
data = pandas.read_csv("50_states.csv")
s = turtle.Screen()

'''Map'''
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)
num=0

'''Turtle Object to print Gameover'''
final = turtle.Turtle()
final.hideturtle()

'''Loop for iterating and getting the input everytime'''
while(1):
    inp = s.textinput(prompt="enter country name",title=f"guessed{num}/50")
    inp = inp.title()
    print(inp)
    if(inp=="Exit"):
        final.penup()
        final.goto(-100,0)
        final.write("GAME OVER",font=("Arial", 25, "normal"))
        break

    for i in data["state"]:
        if i == inp:
            t = turtle.Turtle()
            # t.hideturtle()
            t.penup()
            t.goto(int(data[data.state == inp].x),int(data[data.state == inp].y))
            # print(data[data.state == inp].x)
            t.write(inp)
            num+=1
            print(inp)
s.mainloop()
