##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
# Insert your code here to draw the house!
# Roof and Base
Square = drawpad.create_rectangle(260,400,500,200, fill = 'red')
Triangle = drawpad.create_polygon(260,200,370,80,500,200, fill = 'blue')
#Windows and doors
Squarewin1 = drawpad.create_rectangle(290,260,330,220, fill = 'purple')
Squarewin2 = drawpad.create_rectangle(430,260,470,220, fill = 'grey')
Squarewin3 = drawpad.create_rectangle(290,350,330,310, fill = 'orange')
Squarewin4 = drawpad.create_rectangle(430,350,470,310, fill = 'pink')
Rectangledoor = drawpad.create_rectangle(370,400,400,350, fill = 'brown')
#Door handle and Chimney
line1 = drawpad.create_line(440,145,440,80)
line2 = drawpad.create_line(440,80,480,80)
line3 = drawpad.create_line(480,80,480,183)
doorhandle = drawpad.create_rectangle(390,380,400,370, fill = 'black')
#Grass
grass1 = drawpad.create_rectangle(150,460,630,400, fill = 'green')
grass2 = drawpad.create_rectangle(150,400,260,300, fill = 'green')
grass3 = drawpad.create_rectangle(500,400,630,300, fill = 'green')

root.mainloop()