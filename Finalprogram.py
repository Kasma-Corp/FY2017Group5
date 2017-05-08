import Tkinter
import tkMessageBox
from decimal import Decimal

home = Tkinter.Tk()
home.wm_title("Solar Energy Calculator")


#------Solar to Water Calculator------

def ptw():
    ptw = Tkinter.Tk()
    ptw.wm_title("Please input the dimentions of a solar panel in meters.")

    def draw():

        c.delete('all')

        x=width.get()*4
        y=length.get()*4

        c.create_rectangle(x,y,0,0, fill='#000000')
        ptw.after(10,draw)

    

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
        m = float(Q)/(float(335200))

        tkMessageBox.showinfo("Results", "You can boil " + str(m) +" Litres of room temperature water per minute.")

    def kill():
        ptw.destroy()


    c = Tkinter.Canvas(ptw, width=200, height=200)

    length = Tkinter.Scale(ptw, from_=50, to=0)
    width = Tkinter.Scale(ptw, from_=0, to=50, orient = Tkinter.HORIZONTAL)

    ptoe  = Tkinter.Button(ptw, text="Run Calculation", command = paneltoenergy)
    kill = Tkinter.Button(ptw, text="Return Home", command = kill)

    length.grid(row=2, column = 2)
    width.grid(row=3, column = 3)
    ptoe.grid(row=4, column = 3)
    c.grid(row=2, column = 3)
    kill.grid(row=5, column = 3)

    ptw.after(10, draw)

#------Water to Panel Calculator------
def wtp():
    wtp = Tkinter.Tk()
    wtp.wm_title("Please input the volume of water you would like to boil from room temperature per minutem, in litres.")
    

    def draw2():
        c2.delete('all')

        x = 500
        y = (265 - volume.get()*53)

        c2.create_rectangle(x,y,0,0, fill='white')
        wtp.after(10,draw2)
        
    def calor_output_e():
        m = volume.get()
        q=m*(4190)*(80)

        raw = q*2
        dimen = raw/1850
    

        
        tkMessageBox.showinfo("Results", "You will need a solar panel of " + str(dimen) + " meters squared to boil " + str(m) + " Litres of room temperature water per minute.")

    def killwtp():
        wtp.destroy()

    c2 = Tkinter.Canvas(wtp, width=200, height=200)
    c2.pack()
    c2.configure(background='SteelBlue1')

    volume = Tkinter.Scale(wtp, from_=0, to=5, orient = Tkinter.HORIZONTAL, resolution = 0.01)
    coe  = Tkinter.Button(wtp, text="Run Calculation", command = calor_output_e)
    back = Tkinter.Button(wtp, text="Return Home", command = killwtp)

    volume.pack()
    coe.pack()
    back.pack()

    wtp.after(10, draw2)
#------Theory------

def theoryroot():
    theoryroot = Tkinter.Tk()
    theoryroot.wm_title("Learning The Theory")

    def kill():
        theoryroot.destroy()

#------water to panel theory------

    def wtoptheory():
        wtp = Tkinter.Tk()
        wtp.wm_title("Water volume to panel size theory")

        def killwtop():
            wtp.destroy()

        def s1():
            tkMessageBox.showinfo(title="Step One", message="You start by considering how much water you want to boil from room temperature per minute.")

        def s2():
            tkMessageBox.showinfo(title="Step Two", message="Plug these values into the specific heat capacity equation (Q=m*c*deltaT) to find how much energy that would need.")

        def s3():
            tkMessageBox.showinfo(title="Step Three", message="Convert the energy per minute value to a value of Watts.")

        def s4():
            tkMessageBox.showinfo(title="Step Four", message="Calculate the total energy from the sun using the equation: lowercase sigma*A*T**4, and consider the fact that this is distributed over the full spherical surface of the Earth.")

        def s5():
            tkMessageBox.showinfo(title="Step FIve", message="Now do your energy value divided by two to take atmospheric loss into consideration, and divide this bnew value by the total energy from the sun. You know have a value of solar panel size in meters squared!")

        stepone = Tkinter.Button(wtp, text='Step One', command = s1)
        steptwo = Tkinter.Button(wtp, text='Step Two', command = s2)
        stepthree = Tkinter.Button(wtp, text='Step Three', command = s3)
        stepfour = Tkinter.Button(wtp, text = 'Step Four', command = s4)
        stepfive = Tkinter.Button(wtp, text = 'Step Five', command = s5)
        back = Tkinter.Button(wtp, text = 'Back', command = killwtop)

        stepone.pack()
        steptwo.pack()
        stepthree.pack()
        stepfour.pack()
        stepfive.pack()

        back.pack()

#----panel to water theory-----

    def ptowtheory():
        ptw = Tkinter.Tk()
        ptw.wm_title("Panel Size to Water Volume Theory")

        def killptow():
            ptw.destroy()

        def s1():
            tkMessageBox.showinfo(title="Specific Heat Capacity", message="Assuming that the average energy radiated by the sun per square metre is 1850 W, we multiply the dimensions of the solar panel by the energy per square metre.")

        def s2():
            tkMessageBox.showinfo(title="Step Two", message="Next we must consider the efficiency of the atmosphere which is approximately 50%. To find the energy transferred from the panel, we must multiply the incident energy by 0.5")

        def s3():
            tkMessageBox.showinfo(title="Step Three", message="To find the amount of water that can be boiled, we take the energy transferred from the solar panel, and divide the value by the product of water's specific heat capacity (4200 W/kgK) and the change in temperature. The mass of the water is also the volume in litres")
    
        button1 = Tkinter.Button(ptw, text='Step One', command = s1)
        button2 = Tkinter.Button(ptw, text='Step Two', command = s2)
        button3 = Tkinter.Button(ptw, text='Back', command = killptow)
        button4 = Tkinter.Button(ptw, text='Step Three',command = s3)

        button1.pack()
        button2.pack()
        button4.pack()
        button3.pack()


    a = Tkinter.Button(theoryroot, text = "Panel to Water", command = ptowtheory)
    b = Tkinter.Button(theoryroot, text = "Water to Panel", command = wtoptheory)
    c = Tkinter.Button(theoryroot, text = "Return Home", command = kill)

    a.pack()
    b.pack()
    c.pack()

    

    


pantowat = Tkinter.Button(home, text = "Calculate a volume of water from a size of solar panel", command = ptw)
tr = Tkinter.Button(home, text = "Learn how it all works", command = theoryroot)
wattopan = Tkinter.Button(home, text = "Calculate the dimentions of a solar panel from a volume of water to boil per minute", command = wtp)


pantowat.pack()
wattopan.pack()
tr.pack()

home.mainloop()
