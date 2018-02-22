import turtle

line = turtle.Turtle()


def draw_square(line, window):
    #instantiates turtle object
    line.shape("turtle")
    line.color("white")
    line.speed(10)

    i=0
    while(i < 4):
        line.forward(200)
        line.right(90)
        i = i+1

def draw_shapes(window):


    line2 = turtle.Turtle()
    line2.color("red")
    line2.circle(100)

    line3 = turtle.Turtle()

    line3.color("yellow")
    line3.forward(100)
    line3.left(90)
    line3.forward(100)
    line3.left(90 + 45)
    line3.forward(135)


window = turtle.Screen()
window.bgcolor("black")
for i in range (1,37):
    draw_square(line,window)
    line.right(10)
window.exitonclick()

