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
        
        canvas.delete("all")

    def move(self,canvas):
        self.erase(canvas)
        self.x=self.x+self.dx
        self.y=self.y+self.dy
        self.create(canvas)
        if (self.x>=canvas.winfo_width()):
            self.dx=-5
        if (self.x<=0):
            self.dx=5
        if (self.y>=canvas.winfo_height()):
            self.dy=-1
        if (self.y<=0):
            self.dy=1
            
    def keymove(self,canvas,a):
        if a=="Right":
            if (self.x<=canvas.winfo_width()):
                self.erase(canvas)
                self.x+=5;
                self.create(canvas)

        if a=="Left":
            if (self.x>=0):
                self.erase(canvas)
                self.x+=-5;
                self.create(canvas)

        if a=="Up":
            if (self.y>=0):
                self.erase(canvas)
                self.y+=-5
                self.create(canvas)

        if a=="Down":
            if (self.y<=canvas.winfo_height()):
                self.erase(canvas)
                self.y+=5
                self.create(canvas)

        


    




Car_b =Car(100,30,5,5,"blue",1,)


def key_event(e):
   Car_b.keymove(canvas,e.keysym)








root = tk.Tk()
root.geometry("600x600")



canvas =tk.Canvas(root,width =600,height =600,bg="white")
canvas.place(x=0,y=0)
Car_b.create(canvas)
root.bind("<KeyPress>", key_event)


root.mainloop()