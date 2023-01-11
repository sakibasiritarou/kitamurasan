#coding:utf-8
import tkinter as tk

class A:
    def __init__(self,x,y,dx,dy,color,size):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.color =color 
        self.size = size
    

    def erase(self,canvas):
        
        canvas.delete("all")
    
    def draw(self, canvas):
        canvas.create_rectangle((self.x, self.y), (self.x+30*self.size, self.y+20*self.size),fill=self.color,width=0)
        canvas.create_rectangle((self.x-25*self.size, self.y+20*self.size), (self.x+55*self.size, self.y+40*self.size),fill=self.color,width=0)


    
class Ball:

    def __init__(self,x,y,dx,dy,color,size):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.color =color 
        self.size = size
        self.id = None

    def draw(self, canvas):
        self.id = canvas.create_oval(self.x-20*self.size,self.y-20*self.size,self.x+20*self.size,self.y+20*self.size,fill=self.color,width=0)

    def move(self,canvas):
        canvas.move(self.id, 0, self.dy)
    
    

a=A(250,500,1,1,"green",1.5)


"""
def loop():
    b.move(canvas)
    a.draw(canvas)

    root.after(10,loop)
"""
balls = []

def key_event(e):
    global balls
    b = Ball(270,470,1,-5,"black",0.5)
    
    b.draw(canvas)
    balls.append(b)
    
    # b.loop()    
    


root = tk.Tk()
root.geometry("600x600")

canvas =tk.Canvas(root,width =600,height =600,bg="white")
canvas.place(x=0,y=0)

def update():
    for b in balls:
        b.move(canvas)
    root.update()
    root.after(10, update)


a.draw(canvas)
root.bind("<KeyPress>", key_event)

update()

root.mainloop()