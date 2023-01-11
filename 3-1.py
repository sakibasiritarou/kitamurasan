#coding:utf-8
import tkinter as tk

class Car:
    def __init__(self,x,y,dx,dy,color,size):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.color =color 
        self.size = size
        

    def create(self,canvas):
        canvas.create_rectangle((self.x, self.y), (self.x+30*self.size, self.y+20*self.size),fill=self.color,width=0)
        canvas.create_rectangle((self.x-25*self.size, self.y+20*self.size), (self.x+55*self.size, self.y+40*self.size),fill=self.color,width=0)

        canvas.create_oval(self.x-15*self.size, self.y+40*self.size,self.x+3*self.size, self.y+60*self.size,fill="black",width=0)
        canvas.create_oval(self.x+30*self.size, self.y+40*self.size,self.x+47*self.size, self.y+60*self.size,fill="black",width=0)


    def erase(self,canvas):
        """
        canvas.create_rectangle((self.x, self.y), (self.x+30*self.size, self.y+20*self.size),fill="white",width=0)
        canvas.create_rectangle((self.x-25*self.size, self.y+20*self.size), (self.x+55*self.size, self.y+40*self.size),fill="white",width=0)

        canvas.create_oval(self.x-15*self.size, self.y+40*self.size,self.x+3*self.size, self.y+60*self.size,fill="white",width=0)
        canvas.create_oval(self.x+30*self.size, self.y+40*self.size,self.x+47*self.size, self.y+60*self.size,fill="white",width=0)
        """
        canvas.delete("all")

    def move(self,canvas):
        self.erase(canvas)
        self.x=self.x+self.dx
        self.create(canvas)
        if (self.x>=canvas.winfo_width()):
            self.dx=-5
        if (self.x<=0):
            self.dx=5


Car_b =Car(0,30,5,5,"blue",2,)

def loop():
    Car_b.move(canvas)
    root.after(10,loop)







root = tk.Tk()
root.geometry("600x600")



canvas =tk.Canvas(root,width =600,height =600,bg="white")
canvas.place(x=0,y=0)

root.after(10,loop)



root.mainloop()