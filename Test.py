import Tkinter

main = Tkinter.Tk()

#assuming the panel is on the equator and sunlight hits at the normal to the panel constantly 



def check_float(y):

    try:
        val = int(y)
        return float(y)
        
    except ValueError:
        print("Ooops! You did not enter a number.")
        error.append(1)



def paneltoenergy():
    global error
    error = []


    panellength=check_float(raw_input("Panel Length:"))
    panelwidth=check_float(raw_input("Panel Width:"))

    #Total energy from sun is 1850 watts per square meter

    while error == []:
        size = panellength*panelwidth

        raw_energy = size*1850

        #assuming that half of the energy is lost into the atmosphere

        energy_output = raw_energy/2

        def calor_input_e(c=4.19, t=20):
            Q = energy_output
            t = check_float(raw_input("Please enter the temperature of the water: "))
            while error == []:
                m = Q/(c*(100-t))
                return m
            else:
                print "Please try again, and enter only numbers."

        print "You will be able to boil " + str(calor_input_e()) + " litres of water."
        break
    else:
        print "Please try again, and enter only numbers."


def energytopanel():
    global error
    error = []

    def calor_output_e(m=1.57,c=4.19,t=20):
        m = check_float(raw_input("Please enter how many litres of water there are: "))
        t = check_float(raw_input("Please enter the temperature: "))
        while error == []:
            global q
            q=m*c*(100-t)
            break
        else:
            print "Please try again, and enter only numbers."
            

    calor_output_e()
      
    while error == []:
        
        energyinput = q

        raw_energy=energyinput*2

        size = (raw_energy / 1850)

        squares = str(size)

        print "You will need " + str(squares) + " metres squared of solar panels."
        break
    else:
        print "Please try again, and enter only numbers."

ptoe  = Tkinter.Button(main, text="Panel To Energy", command = paneltoenergy)
etop = Tkinter.Button(main, text="Energy to Panel", command = energytopanel)

ptoe.pack()
etop.pack()

main.mainloop()

