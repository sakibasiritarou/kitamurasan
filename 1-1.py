#coding:utf-8
import tkinter as tk

x=100
y=100

root = tk.Tk()
root.geometry("600x400")



canvas =tk.Canvas(root,width =600,height =400,bg="white")
canvas.place(x=0,y=0)

canvas.create_rectangle(x,y,x+200,y+30,fill="black",width=100)

root.mainloop()