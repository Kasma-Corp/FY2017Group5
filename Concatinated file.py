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

    def calor_input_e(c=4.19, t=20):
        Q = energy_output
        t = float(raw_input("Please enter the temperature of the water. "))

        m = Q/(c*(100-t))

        return m

    print "You will be able to boil " + str(calor_input_e()) + " litres of water."



   

def energytopanel():

    energyinput=input("Energy Required:")

    raw_energy=energyinput*2

    size = (raw_energy / 1850)

    squares = str(size)

    print "You will be able to boil " + str(calor_input_e()) + " litres of water."

ptoe  = Tkinter.Button(main, text="Panel To Energy", command = paneltoenergy)
etop = Tkinter.Button(main, text="Energy to Panel", command = energytopanel)

ptoe.pack()
etop.pack()

main.mainloop()



def calor_output_e(m=1.57,c=4.19,t=20):
    m = float(raw_input("Please enter how many litres of water there are. "))
    t = float(raw_input("Please enter the temperature. "))
    q=m*c*(100-t)
    return q



print "You will need the following amount of energy (in Joules) " + str(calor_output_e()) + " to boil the water."



    

    

