
import math
import turtle




# Question-1

# def distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#
# def midpoint(x1, y1, x2, y2):
#     return ((x1 + x2)/2, (y1 + y2)/2)


# # Take input of coordinates for two points
# x1, y1 = map(int, input("Enter coordinates for first point (x1,y1): ").split(","))
# x2, y2 = map(int, input("Enter coordinates for second point (x2,y2): ").split(","))
#
# # Initialize turtle and set up the screen
# t = turtle.Turtle()
# t.speed(0)
# turtle.setup(600, 600)
# turtle.setworldcoordinates(-10, -10, 110, 110)
#
# # Draw the x and y axes
# t.pensize(2)
# t.penup()
# t.goto(0,0)
# t.pendown()
# t.goto(100,0)
# t.penup()
# t.goto(0,0)
# t.pendown()
# t.goto(0,100)
#
# # Plot the two points
# t.penup()
# t.goto(x1, y1)
# t.dot(10, "red")
# t.write("A", align="left")
# t.goto(x2, y2)
# t.dot(10, "blue")
# t.write("B", align="left")
#
# # Draw the line between the two points
# t.pensize(1)
# t.penup()
# t.goto(x1, y1)
# t.pendown()
# t.goto(x2, y2)
#
# # Calculate the distance and midpoint
# dist = distance(x1, y1, x2, y2)
# mid = midpoint(x1, y1, x2, y2)
#
# # Plot the midpoint
# t.penup()
# t.goto(mid[0], mid[1])
# t.dot(10, "green")
# t.write("Midpoint", align="left")
#
# # Display the distance
# t.penup()
# t.goto((x1+x2)/2, (y1+y2)/2+10)
# t.write("Distance: {:.2f}".format(dist), align="center")
#
# # Keep the window open until user closes it
# turtle.done()


#Question -2

# import turtle
#
# # Define the center coordinates
# x, y = 0, 0
#
# # Define the radii of the circles
# radii = [50, 75, 100, 125, 150]
#
# # Initialize turtle and set up the screen
# t = turtle.Turtle()
# t.speed(0)
# turtle.setup(600, 600)
# turtle.setworldcoordinates(-200, -200, 200, 200)
#
# # Draw the x and y axes
# t.pensize(2)
# t.penup()
# t.goto(-200,0)
# t.pendown()
# t.goto(200,0)
# t.penup()
# t.goto(0,-200)
# t.pendown()
# t.goto(0,200)
#
# # Draw the circles
# t.pensize(1)
# for r in radii:
#     t.penup()
#     t.goto(x, y-r)
#     t.pendown()
#     t.circle(r)
#
# # Keep the window open until user closes it
# turtle.done()



#Question-3

# import turtle
# import math
#
# t = turtle.Turtle()
#
# sides = 5
# length = 150
#
# angle = 360 / sides
#
# t.penup()
# t.goto(-length / 2, -(length / 2) * math.tan(math.radians(54)))
# t.pendown()
#
# for i in range(sides):
#     t.forward(length)
#     t.left(angle)
#
# dfc = (length / 2) / (math.cos(math.radians(54)))  # dfc=distance from centre (0,0)
#
# t.fillcolor("red")
# t.begin_fill()
# t.home()
# t.goto(length / 2, -(length / 2) * math.tan(math.radians(54)))
# t.end_fill()
# t.fillcolor("yellow")
# t.begin_fill()
# t.home()
# t.goto(dfc * math.cos(math.radians(18)), dfc * math.sin(math.radians(18)))
# t.end_fill()
# t.fillcolor("blue")
# t.begin_fill()
# t.home()
# t.goto(0, dfc)
# t.end_fill()
# t.fillcolor("gray")
# t.begin_fill()
# t.home()
# t.goto(-dfc * math.cos(math.radians(18)), dfc * math.sin(math.radians(18)))
# t.end_fill()
# t.fillcolor("green")
# t.begin_fill()
# t.home()
# t.goto(-length / 2, -(length / 2) * math.tan(math.radians(54)))
# t.end_fill()
#
# turtle.done()



#Question -4

# from PIL import Image
#
# inp = Image.open('colored.jpg').convert('L')
#
# threshold_value = 128
#
# # convert to binary image
# binary = inp.point(lambda x: 255 if x > threshold_value else 0, '1')
#
# binary.save('colored.png')


# #Question-5

from PIL import Image

# Open the image
img = Image.open("/Users/harshvardhan/Desktop/nit_sem_4/Labs/python/Experiment-10/colored.jpg")

# Extract the RGB values of each pixel in the image
pixels = img.load()
width, height = img.size
rgb_pixels = []
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        rgb_pixels.append((r, g, b))

# Print the RGB pixel values
print(rgb_pixels)











