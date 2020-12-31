from turtle import *
from shapes import *
from tkinter import *
from playsound import playsound
# from Tkinter import *
# import tkSnack
# cannot find the projectimport playsound
# done()
# from playsound import playsound
# from gtts import gTTS

myPen = Turtle()
myPen.shape("turtle")
# myPen.tracer(0)
myPen.hideturtle()
myPen.speed(10)
wn = turtle.Screen()
wn.bgcolor('#69D9FF')
wn.title('Birthday Cake')
y = -140

'''def playaudio(audio):
    playsound(audio)

def convert_to_audio(text):
    audio = gTTS(text)
    audio.save("textaudio.mp3")
    playaudio("textaudio.mp3")
    convert_to_audio("Happy Birthday Harriet")

'''
# Initialize the dictionary
ingredients = {}
# Add itemms to the dictionary
# ingredients["cake_flour"] = "#306998"
# ingredients["cocoa_powder"] = "#f3e5ab"
# ingredients["sugar"] ="#FFFFFF"
# ingredients["salt"] = "#FFFFFF"
# ingredients["baking_powder"] = "#646464"
# ingredients["baking_soda"]  = "#FFFFFF"
ingredients["eggs"] = "#00FF00"
ingredients["vanilla_extract"] = "#FF0000"
ingredients["cream_milk"] = "#00FF00"
# ingredients["vegetable_oil"] = "#FFFDC4"
# ingredients["hot_water"] = "#FFFDC4"
# ingredients["white_vinegar"] = "#FFFDC4"
# ingredients["balloon"] = "#00FF00"

# initialize the list of layers
layers = []

# Add values to the list
# layers.append(["cake_flour", 20])
# layers.append(["cocoa_powder", 10])
# layers.append(["sugar", 20])
# layers.append(["salt",10])
# layers.append(["baking_powder", 10])
# layers.append(["baking_soda", 10])
layers.append(["eggs", 10])
layers.append(["vanilla_extract", 10])
layers.append(["cream_milk", 20])
# layers.append(["vegetable_oil", 10])
# layers.append(["vanilla_extract", 5])
# layers.append(["hot_water", 10])
# layers.append(["balloon", 5])
# preview the content of the list
print(layers)

###now lets preview the layer cake
# lets draw the plate


draw_rectangle(myPen, "blue", -150, y - 10, +300, 10)

# iterate through each layer of the list

for layer in layers:
    # draw_rectangle(myPen, ingredients[layer[0]], -120, y, 240, layer[1])
    draw_square(myPen, 'green', -70, y, 140)
    y += layer[1]
# addVanilla(myPen, ingredients["vanilla_extract"],7,y+160,14)
addEggs(myPen, ingredients["eggs"], y + 120)
#playsound('/home/harriet/Desktop/Best Happy Birthday Song .MP3')
playsound('/home/harriet/Desktop/Happy birthday - Acappella.MP3')
draw_square(myPen, 'yellow', -50, y + 130, 100)
addCream_milk(myPen, ingredients["cream_milk"], y + 230)
addVanilla(myPen, ingredients["vanilla_extract"], 3, y + 240, 6)
# balloon(myPen, ingredients["balloon"],2,y,4)
playsound('/home/harriet/Desktop/Happy birthday - Acappella.MP3')
myPen.getscreen().update()

done()

# addVanilla(myPen, ingredients["vanilla_extract"], 7, y + 160, 14)

