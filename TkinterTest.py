#!/usr/bin/env python
from ttk import Frame, Button, Style
from Tkinter import Tk, BOTH
import tkMessageBox as box
from Tkinter import *

reminderFilePath = ("/Users/Callum/Desktop/Scripts/Test/Reminders.txt")
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.VarEntRemind = StringVar()
        self.parent.title("Reminders")
        self.pack()
        add = Button(self, text = "Add reminder", command = self.send).grid(row = 3, column = 1)
        show = Button(self, text = "Show reminders", command = self.onShow).grid(row = 3, column = 0)
        self.EntRemind = Entry(self, textvariable = self.VarEntRemind).grid(row = 0, column = 1)
        label = Label(self, text = "Please enter reminder:").grid(row = 0)
    def onShow(self):
        self.createWindow()

    def send(self):
        box.showinfo("Information", "Reminder added to file")
        print("Added the reminder to the file!")
        U = self.VarEntRemind.get()
        with open(reminderFilePath, 'a') as fout:
            fout.write(U + "\n")
            fout.close()
        self.clear_text()

    def clear_text(self):
        self.EntRemind.delete(0, 'end')

    def clear():
        text.delete("1.0", END)

    def createWindow(self):
        win = Toplevel(self)
        file = open(reminderFilePath)
        data = file.read()
        file.close()
        Results = Label(win, text = data).grid(row = 0, column = 1)
        b1 = Button(win, text = "Ok", command = win.destroy).grid(row = 1, column = 1)
        
 
def main():
    master = Tk()
    ex = Example(master)
    master.mainloop()
if __name__ == '__main__':
    main()
