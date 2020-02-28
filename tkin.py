from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("hello")
#root.geometry("400x400")
def hello():
	messagebox.showinfo("hello every one","hello")

button= Button(root,bg="black",fg="white",text="hello",command=hello)
button.pack(side="left",fill=X)
root.mainloop()
