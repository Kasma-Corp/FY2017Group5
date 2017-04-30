import Tkinter
import tkMessageBox


main_window = Tkinter.Tk()

topFrame = Tkinter.Frame(main_window)
bottomFrame = Tkinter.Frame(main_window)

topFrame.pack()
bottomFrame.pack(side='bottom')

def s1():
    tkMessageBox.showinfo(title="Specific Heat Capacity", message="Assuming that the average energy radiated by the sun per square metre is 925 W, we multiply the dimensions of the solar panel by the energy per square metre.")

def s2():
    tkMessageBox.showinfo(title="Step Two", message="Next we must consider the efficiency of the panel which is approximately 5%. To find the energy transferred from the panel, we must multiply the incident energy by 0.05")

def s3():
    tkMessageBox.showinfo(title="Step Three", message="To find the amount of water that can be boiled, we take the energy transferred from the solar panel, and divide the value by the product of water's specific heat capacity (4200 W/kgK) and the change in temperature. The mass of the water is also the volume in litres")
    
button1 = Tkinter.Button(topFrame, text='Step One', command = s1)
button2 = Tkinter.Button(topFrame, text='Step Two', command = s2)
button3 = Tkinter.Button(bottomFrame, text='Back')
button4 = Tkinter.Button(topFrame, text='Step Three',command = s3)

button1.pack()
button2.pack()
button3.pack()
button4.pack()


main_window.mainloop()
