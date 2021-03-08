import turtle  # import turtle to draw


def DrawStar():  # defining my function
    turtle.hideturtle()  # hiding the turtle
    turtle.pencolor("blue")  # setting the pen colour to blue
    turtle.pensize(20)   # making the pensize to 20
    turtle.penup()         # picking then pen up
    turtle.goto(-200, 100)  # picking the location i want the drawing to start at
    turtle.pendown()        # putting the pen down so i can start drawing in this location
    for i in range(5):      # for loop do execute my drawing
        turtle.forward(400)  # telling the turtle to go forward 400
        turtle.right(144)   # telling the turtle to go right at a angle of 144 degrees
    turtle.exitonclick()    # termination of the program


if __name__ == '__main__':
    DrawStar()      # running my function
