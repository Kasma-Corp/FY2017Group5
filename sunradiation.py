import Tkinter

main = Tkinter.Tk()

#assuming the panel is on the equator and sunlight hits at the normal to the panel constantly 

def paneltoenergy():

    panellength=input("Panel Length:")
    panelwidth=input("Panel Width:")

    #Total energy from sun is 1850 watts per square meter

    size = panellength*panelwidth

    raw_energy = size*1850

    #assuming that half of the energy is lost into the atmosphere

    energy_output = raw_energy/2

    print energy_output

def energytopanel():

    energyinput=input("Energy Required:")

    raw_energy=energyinput*2

    size = (raw_energy / 1850)

    squares = str(size)

    print squares + " meters squared"

ptoe  = Tkinter.Button(main, text="Panel To Energy", command = paneltoenergy)
etop = Tkinter.Button(main, text="Energy to Panel", command = energytopanel)

ptoe.pack()
etop.pack()

main.mainloop()
