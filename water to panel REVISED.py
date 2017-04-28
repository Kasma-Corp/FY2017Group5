import Tkinter
import tkMessageBox


main_window = Tkinter.Tk()

topFrame = Tkinter.Frame(main_window)
bottomFrame = Tkinter.Frame(main_window)

topFrame.pack()
bottomFrame.pack(side='bottom')

def s1():
    tkMessageBox.showinfo(title="Step One", message="You start by considering how much water you want to boil from room temperature.")

def s2():
    tkMessageBox.showinfo(title="Step Two", message="Plug these values into the specific heat capacity equation (Q=m*c*deltaT) to find how much energy that would need.")

button1 = Tkinter.Button(topFrame, text='Step One', command = s1)
button2 = Tkinter.Button(topFrame, text='Step Two', command = s2)
button3 = Tkinter.Button(bottomFrame, text='Back')

button1.pack()
button2.pack()
button3.pack()


main_window.mainloop()
