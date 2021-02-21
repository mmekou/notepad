from tkinter import Text, Tk

r = Tk()
r.title("Notepad")
r.geometry("400x400")

t = Text(r, height=60, width=1000)
t.pack()

r.mainloop()