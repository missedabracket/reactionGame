from guizero import App, Waffle, info, Combo
import random, time
#Action where a pixel on waffle is clicked
def clicked(x,y):
    print(x,y)
    if xTarget == x and yTarget == y:
        end=time.time()
        delay = end-start
        info("Hit","You hit the target. It took %4.2f seconds " %delay)
        myWaffle.set_all("red")
        myWaffle.after(300,pickPixel)
    else:
        myWaffle.set_pixel(x,y,"white")

def pickPixel():
    global xTarget, yTarget, start
    xTarget = random.randint(0,myWaffle.height-1)
    yTarget = random.randint(0,myWaffle.width-1)
    myWaffle.set_pixel(xTarget,yTarget,"red")
    start = time.time()
    print("Target is ",xTarget,yTarget)

def setDifficulty(d):
    if d == "Easy":
        myWaffle.height = 5
        myWaffle.width = 5
    elif d == "Medium":
        myWaffle.height = 10
        myWaffle.width = 10
    else:
        myWaffle.height = 20
        myWaffle.width = 20
    #Carry out action after 3 seconds
    myWaffle.show()
    myWaffle.after(300,pickPixel)

#Make a window
window1 = App(title="Waffle",width=600,height=600)
#Make a waffle and set properties
myWaffle = Waffle(window1,20,20,20,3,"red",command=clicked)
myWaffle.hide()
#Display options for game
gameOptions = Combo(window1,["Easy","Medium","Hard"],command=setDifficulty)
#display the window
window1.display()