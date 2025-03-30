from turtle import *

speed(7)
width(10)
color("yellow")

#

forward(200) 
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)


#draw a door

left(90)
forward(70)
color("blue")
begin_fill()
left(90)
forward(90)
right(90)
forward(70)
right(90)
forward(90)
end_fill()


#draw a roof
penup()
goto(200, 200)
pendown()
color("purple")
begin_fill()
right(130)
forward(130)
left(80)
forward(130)
end_fill()



# draw svindows
penup()
goto(10, 150)
pendown()
begin_fill()
left(50)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)



#--- second
penup()
goto(190, 150)
pendown()
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)

end_fill()

exitonclick()











