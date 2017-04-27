import Tkinter
import tkMessageBox

main = Tkinter.Tk()
main.wm_title("Please input the dimentions of your solar panel in meters:")
c = Tkinter.Canvas(main, width=200, height=200)


#assuming the panel is on the equator and sunlight hits at the normal to the panel constantly 

def draw():

    c.delete('all')

    x=width.get()*4
    y=length.get()*4

    c.create_rectangle(x,y,0,0, fill='#000000')
    main.after(10,draw)

def paneltoenergy():

    panellength=length.get()
    panelwidth=width.get()
    

    #Total energy from sun is 1850 watts per square meter

    size = panellength*panelwidth

    raw_energy = size*1850

    #assuming that half of the energy is lost into the atmosphere

    energy_output = raw_energy/2

    #calorimitry begins here

    Q = energy_output
    m = Q/(4.184*80)

    tkMessageBox.showinfo("Results", "You can boil " + str(m) +" Litres of room temperature water.")


    

length = Tkinter.Scale(main, from_=50, to=0)
width = Tkinter.Scale(main, from_=0, to=50, orient = Tkinter.HORIZONTAL)



ptoe  = Tkinter.Button(main, text="Run Calculation", command = paneltoenergy)

length.grid(row=2, column = 2)
width.grid(row=3, column = 3)
ptoe.grid(row=4, column = 3)
c.grid(row=2, column = 3)

main.after(10, draw)

main.mainloop()
