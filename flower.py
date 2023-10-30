# from turtle import *
# import colorsys

# speed(0)
# bgcolor("black")
# h = 0

# for i in range(16):
#     for j in range(18):
#         c = colorsys.hsv_to_rgb(h, 1, 1)
#         color(c)
#         h += 0.005
#         rt(90)
#         circle(150 - j * 6, 90)
#         lt(90)
#         circle(150 - j * 6, 90)
#         rt(180)
#         circle(40, 24)

# done()

from turtle import *
import colorsys

speed(0)
bgcolor("black")

# Function to draw a colorful flower
def draw_flower(petals, radius, angle):
    for _ in range(petals):
        color(colorsys.hsv_to_rgb(angle, 1, 1))
        begin_fill()
        circle(radius, 60)
        left(120)
        circle(radius, 60)
        left(120 + 360 / petals)
        end_fill()
        angle += 0.02  # Adjust this value to change the color variation

# Set initial parameters
petals = 12  # Number of petals
flower_radius = 100  # Radius of the flower
color_angle = 0.0

# Position the turtle
penup()
goto(0, -150)
pendown()

# Draw the flower
draw_flower(petals, flower_radius, color_angle)

# Hide the turtle and display the result
hideturtle()
done()

