#coding:utf-8
import tkinter as tk


root = tk.Tk()
root.geometry("600x400")



canvas =tk.Canvas(root,width =600,height =400,bg="white")
canvas.place(x=0,y=0)

canvas.create_rectangle((55, 60), (85, 80),fill="black",width=10)
canvas.create_rectangle((30, 80), (110, 100),fill="black",width=15)
canvas.create_oval(40,105,60,125,fill="black",width=0)
canvas.create_oval(85,105,105,125,fill="black",width=0)
canvas.create_text(55,130,text="Yuito Komeda")

root.mainloop()