#!/usr/bin/env python
import os, time
from ttk import Frame, Button, Style
from Tkinter import Tk, BOTH
import tkMessageBox as box
from Tkinter import *

reminderFilePath = os.path.expanduser("~/.Reminder.txt")

class PopupGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.VarEntRemind = StringVar()
        self.parent.title("Reminders")
        self.pack()
        add = Button(self, text = "Add reminder", command = self.send)
        deleteIt = Button(self, text = "Delete all reminders", command = self.createConfirmWin)
        close = Button(self, text = "Quit", command = self.onQuit)
        show = Button(self, text = "Show reminders", command = self.onShow)
        self.EntRemind = Entry(self, textvariable = self.VarEntRemind)
        label = Label(self, text = "Please enter reminder:")
        sleep = Button(self, text = "Sleep", command = self.createSleepWin)
        add.grid(row = 1, column = 1)
        show.grid(row = 1, column = 0)
        self.EntRemind.grid(row = 0, column = 1)
        label.grid(row = 0)
        deleteIt.grid(row = 0, column = 2)
        close.grid(row = 1, column = 2)
        sleep.grid(row = 2, column = 1)


    def createConfirmWin(self):
        newWin = Toplevel(self)
        agree = Button(newWin, text = "Yes", command = self.onDelete)
        deny = Button(newWin, text = "No", command = lambda: newWin.destroy())
        label = Label(newWin, text = "Are you sure you want to delete all reminders?")
        label.grid(row = 0, column = 0)
        agree.grid(row = 0, column = 1)
        deny.grid(row = 0, column = 2)
        
    def createSleepWin(self):
        newWin = Toplevel(self)
        newWin.title("Sleep time")
        self.sleepSlider = Scale(newWin,length = 300, orient = 'horizontal', from_=0, to_=120)
        sleepLabel = Label(newWin, text = "Set when you want to be reminded again(seconds):")
        sleepButton2 = Button(newWin, text = "Sleep now!", command = self.onSleep)
        closeWin = Button(newWin, text = "Close", command = lambda: newWin.destroy())
        closeWin.grid(row = 2, column = 0)
        sleepLabel.grid(row = 0, column = 0)
        self.sleepSlider.grid(row = 1, column = 0)
        sleepButton2.grid(row = 0, column = 1)
        

    def onSleep(self):
        U = self.sleepSlider.get()
        if os.path.exists:
            time.sleep(U)
            self.onShow()
            print("I slept!")


    def clear(self):
        self.EntRemind.delete(0, END)

    def onShow(self):
        if os.path.exists(reminderFilePath):
            self.createWindow()
            self.clear()
        else:
            print("The file doesn't exist!")
            box.showinfo("Information", "The file either doesnt exist or can't be found, plese enter a new reminder to create a file.")

            
    def onQuit(self):
        quit()
    
    def onDelete(self):
        self.clear()
        if os.path.exists(reminderFilePath):
            box.showinfo("Information", "All reminders have been deleted")
            os.remove(reminderFilePath)
        else:
            print("Can't delete file as it doesn't exist!")
            box.showinfo("Information", "The file can't be deleted as it doesn't exist")

    def send(self):
        box.showinfo("Information", "Reminder added to file")
        print("Added the reminder to the file!")
        U = self.VarEntRemind.get()
        with open(reminderFilePath, 'a') as fout:
            fout.write(U + "\n")
            fout.close()
        self.clear()

    def createWindow(self):
        win = Toplevel(self)
        file = open(reminderFilePath)
        data = file.read()
        file.close()
        Results = Label(win, text = data).grid(row = 0, column = 1)
        b1 = Button(win, text = "Ok", command = win.destroy).grid(row = 1, column = 1)
        
 
def main():
    master = Tk()
    ex = PopupGUI(master)
    master.mainloop()
if __name__ == '__main__':
    main()

