import turtle
import time

#Initialize turtle
s = turtle.Screen()
t = turtle.Turtle()
s.colormode(255)
s.setup(width = 1.0, height = 1.0)
t.hideturtle()

######Settings######
color1 = 33, 37, 41
color2 = 107, 216, 161
color3 = 56, 138, 178
bg = 248, 249, 250
angle = 100
iterations = 4
values = [0, 60, 0]
scale = 500
showturtle = False
####################
s.bgcolor(bg)
if showturtle == False:
    s.tracer(0,0)

def fractal(angle, iterations, values, scale, speed = 0):
    #Moves to third quadrant, set speed 
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.speed(speed)
    #Def vars
    templist = list(values)
    sideLength = (scale/((iterations) * 2 * ((len(templist)/3)+1)*2))
    #Each iteration
    for i in range(iterations):
        #List multiplies by three
        templist += templist + templist
        #Go through first third of list
        for n in range(int(len(templist)/3)):
            #Modifies value with angle
            templist[n] = templist[n] + angle
        #Go through last third of list
        for n in range(int(len(templist)/3)):
            n = len(templist) - n - 1 
            #Modifies value with angle
            templist[n] = templist[n] - angle
    #Draws using values made in list
    for i in range(len(templist)):
        if i % 3 == 0:
            t.color(color1)
        if i % 3 == 1:
            t.color(color2)
        if i % 3 == 2:
            t.color(color3)
        t.setheading(templist[i])
        t.forward(sideLength)

def fractal2(angle, iterations, values, scale, speed = 0):
    #Moves to third quadrant, set speed 
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.speed(speed)
    #Def vars
    templist = list(values)
    sideLength = (scale/((iterations) * 2 * ((len(templist)/3)+1)*2))
    #Each iteration
    for i in range(iterations):
         #List multiplies by three
        templist += templist + templist
        #Go through first third of list
        for n in range(int(len(templist)/3)):
            #Modifies value with angle
            templist[n] = templist[n] - angle
        #Go through last third of list
        for n in range(int(len(templist)/3)):
            n = len(templist) - n - 1 
            #Modifies value with angle
            templist[n] = templist[n] + angle
    #Draws using values made in list
    for i in range(len(templist)):
        if i % 3 == 0:
            t.color(color1)
        if i % 3 == 1:
            t.color(color2)
        if i % 3 == 2:
            t.color(color3)
        t.setheading(templist[i])
        t.forward(sideLength)        
      
time.sleep(5)    

for i in [75]:
    fractal(i, iterations, values, scale) 
    fractal2(i, iterations, values, scale) 

turtle.update()
input("This is your fractalz, press enter to continue...")
quit()
