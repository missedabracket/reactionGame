from guizero import App, Box, Waffle, info
import random

#Action where a pixel on waffle is clicked
def clicked(x,y):
    print(x,y)
    if xTarget == x and yTarget == y:
        info("Hit","You hit the target")
        myWaffle.set_all("white")
        myWaffle.after(3000,pickPixel)
    else:
        myWaffle.set_all("red")


def pickPixel():
    global xTarget, yTarget
    xTarget = random.randint(0,19)
    yTarget = random.randint(0,19)
    myWaffle.set_pixel(xTarget,yTarget,"red")
    print("Target is ",xTarget,yTarget)


#Make a window
window1 = App(title="Waffle",width=600,height=800)

#Make a waffle and set properties
myWaffle = Waffle(window1,20,20,20,3,"white",command=clicked)

#Carry out action after 3 seconds
myWaffle.after(3000,pickPixel)

#display the window
window1.display()