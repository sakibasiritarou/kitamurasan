#coding:utf-8
import tkinter as tk

class Car:
    def __init__(self,x,y,color,color2,size):
        self.x=x
        self.y=y
        self.color =color 
        self.color2 =color2
        self.size = size
        

    def create(self,canvas):
        canvas.create_rectangle((self.x, self.y), (self.x+30*self.size, self.y+20*self.size),fill=self.color,width=0)
        canvas.create_rectangle((self.x-25*self.size, self.y+20*self.size), (self.x+55*self.size, self.y+40*self.size),fill=self.color,width=0)

        canvas.create_oval(self.x-15*self.size, self.y+40*self.size,self.x+3*self.size, self.y+60*self.size,fill=self.color2,width=0)
        canvas.create_oval(self.x+30*self.size, self.y+40*self.size,self.x+47*self.size, self.y+60*self.size,fill=self.color2,width=0)





root = tk.Tk()
root.geometry("600x600")



canvas =tk.Canvas(root,width =600,height =600,bg="white")
canvas.place(x=0,y=0)





for i in range(10):
    for j in range(10):
        if (i+j)%2==0:
            a=Car(10+j*50,i*50,"red","black",0.5)
            a.create(canvas)
        else:
            b=Car(10+j*50,i*50,"blue","black",0.5)
            b.create(canvas)

Flag =True
while Flag:
    number=input()
    if number.isdigit():
        number_i =int(number)
        if number_i>=0:
            if number_i<100:
             break
            else:
                print('0~99の整数値を入力して下さい。')
        else:
            print('0~99の整数値を入力して下さい。')
    else:
        print('0~99の整数値を入力して下さい。')

s=number_i%10
t=number_i/10
t=int(t)

c=Car(10+s*50,t*50,"white","white",0.5)
c.create(canvas)

        





    


        



root.mainloop()