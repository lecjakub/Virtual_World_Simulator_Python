from tkinter import *

okno = Tk()

okno.title("Jakub Łęcki 175494")
okno.configure(background="red")
plansza = Label(okno, bg="blue", text="Hello World")#.grid(row=2, column=2, sticky=W)
plansza.pack()
okno.mainloop()
