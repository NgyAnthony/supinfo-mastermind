from tkinter import *
import random

root=Tk()
canvas=Canvas(root,width=1000,height=1000)
canvas.pack()

def colorClick(event):
    pos = event.widget.find_closest(event.x, event.y)
    print(color[pos[0] - 1]) 


color = []   
def generate_color_num():
    for i in range(6):
        color.append(random.randint(0, 12))

    print(color)

def generate_color_oval():
    size = 50

    for idx, value in enumerate(color):
        x0 = size * idx + 10 + (idx * 20)
        y0 = 10
        x1 = x0 + size 
        y1 = 60
    
        ovalName = 'oval{}'.format(value)
        canvas.create_oval(x0, y0, x1, y1 ,tags=ovalName,fill='blue')
        canvas.tag_bind(ovalName,'<Button>', colorClick)

generate_color_num()
generate_color_oval()

def close_window():
    root.destroy()

button = Button(text = "quit", command = close_window)
button.pack()

root.mainloop()
