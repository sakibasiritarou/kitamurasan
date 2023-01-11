#coding:utf-8
import tkinter as tk

class Car:
    def __init__(self,x,y,color,size):
        self.x=x
        self.y=y
        self.color =color 
        self.size = size
        

    def create(self,canvas):
        canvas.create_rectangle((self.x, self.y), (self.x+30*self.size, self.y+20*self.size),fill=self.color,width=0)
        canvas.create_rectangle((self.x-25*self.size, self.y+20*self.size), (self.x+55*self.size, self.y+40*self.size),fill=self.color,width=0)

        canvas.create_oval(self.x-15*self.size, self.y+40*self.size,self.x+3*self.size, self.y+60*self.size,fill="black",width=0)
        canvas.create_oval(self.x+30*self.size, self.y+40*self.size,self.x+47*self.size, self.y+60*self.size,fill="black",width=0)

a=Car(55,60,"red",1)

b=Car(200,100,"blue",2)



root = tk.Tk()
root.geometry("600x400")



canvas =tk.Canvas(root,width =600,height =400,bg="white")
canvas.place(x=0,y=0)

a.create(canvas)
b.create(canvas)

root.mainloop()