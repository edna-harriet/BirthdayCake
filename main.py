
from turtle import *
import turtle
from shapes import *

from playsound import playsound

myPen = Turtle()
myPen.shape("turtle")

myPen.hideturtle()
myPen.speed(10)

wn = turtle.Screen()
wn.title('Birthday Cake')
#screen  =  turtle.Screen()
wn.bgpic('/home/harriet/Desktop/hearrt.png')
##bgpic.width=400
#bgpic.height=400
y = -190  #value positions where on the background screen the plate hangs.

# Initialize the dictionary
ingredients = {}
# Add itemms to the dictionary
# ingredients["cake_flour"] = "#306998"
# ingredients["cocoa_powder"] = "#f3e5ab"
# ingredients["sugar"] ="#FFFFFF"

ingredients["eggs"] = "#00FF00"
ingredients["vanilla_extract"] = "#FF0000"
ingredients["cream_milk"] = "#00FF00"
# ingredients["vegetable_oil"] = "#FFFDC4"


# initialize the list of layers
layers = []

# Add values to the list
# layers.append(["cake_flour", 20])
# layers.append(["cocoa_powder", 10])
# layers.append(["sugar", 20])

layers.append(["eggs", 10])
layers.append(["vanilla_extract", 10])
layers.append(["cream_milk", 20])
# layers.append(["vegetable_oil", 10])
# preview the content of the list
print(layers)

###now lets preview the layer cake
# lets draw the plate

draw_rectangle(myPen, "purple", -150, y - 10, +300, 10)# measurements determine how far left or right, up or down the plate takes.

# iterate through each layer of the list

for layer in layers:
    # draw_rectangle(myPen, ingredients[layer[0]], -120, y, 240, layer[1])
    draw_square(myPen, 'green', -70, y, 140) #this is our first cake on the plate
    y += layer[1]


addEggs(myPen, ingredients["eggs"], y + 120) #call this function from shapes.py file

playsound('/home/harriet/Desktop/Happy birthday - Acappella.MP3')# audio file is in my local computer.

draw_square(myPen, 'yellow', -50, y + 130, 100) # #this is our second cake/layer ontop of the first cake/layer.
addCream_milk(myPen, ingredients["cream_milk"], y + 230)#call this function from shapes.py file
addVanilla(myPen, ingredients["vanilla_extract"], 3, y + 240, 6)#call this function from shapes.py file
playsound('/home/harriet/Desktop/Happy birthday - Acappella.MP3')

myPen.getscreen().update()

done()



