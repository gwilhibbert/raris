from tkinter import *
import time

gui = Tk()

gui.geometry("957x503")

c = Canvas(gui ,width=957 ,height=503)

c.pack()

photo = PhotoImage(file="background.png")

c.create_image(957/2,503/2, image=photo)

xcord=10
ycord=10

rectangle = c.create_rectangle(xcord,ycord,xcord+50,ycord+50,outline="red",width=4)

xd = 5

yd = 10
def timer(gui,canvas,duration):
    initial_time=time.time()
    current_time=0
    text=c.create_text(100,710,font=("calibri",30), anchor=SW,text=(int(initial_time)+duration-int(current_time)))
    while current_time<=(initial_time+duration):
        previous_time=current_time
        current_time=time.time()
        if int(previous_time)!=int(current_time):
            #print(int(initial_time)+5-int(current_time))
            canvas.delete(text)
            text=canvas.create_text(100,410,font=("calibri",30), anchor=SW,text=(int(initial_time)+duration-int(current_time)))
            gui.update()
            
        gui.update()
    canvas.delete(text)

position_dictionary={
    "MEK" : [100,100,60],
    "Rinse1" : [100,200,60],
    "Rinse2" : [100,200,60],
    "Rinse3" : [100,200,60],
    "Clean1" : [100,200,60],
    "Clean2" : [100,200,60],
    "Etch" : [100,200,60],
    "Plating" : [100,200,60],
    "Rinse2" : [100,200,60],
    "Rinse2" : [100,200,60],
    "Rinse2" : [100,200,60],
    "Rinse2" : [100,200,60],
    }
while True:
    xcord=100
    ycord=100
    c.coords(rectangle,xcord,ycord,xcord+50,ycord+50)
    gui.update()
    timer(gui,c,5)
    xcord=800
    c.coords(rectangle,xcord,ycord,xcord+50,ycord+50)
    gui.update()
    timer(gui,c,6)
    ycord=400
    c.coords(rectangle,xcord,ycord,xcord+50,ycord+50)
    gui.update()
    timer(gui,c,7)
    xcord=100
    c.coords(rectangle,xcord,ycord,xcord+50,ycord+50)
    gui.update()
    timer(gui,c,8)



# while True:

#   c.move(rectangle,xd,yd)

#   p=c.coords(rectangle)

#   if p[3] >= 800 or p[1] <=0:

#      yd = -yd

#   if p[2] >=800 or p[0] <=0:

#      xd = -xd

#   gui.update()

#   time.sleep(0.025) 

gui.title("First title")

gui.mainloop()
