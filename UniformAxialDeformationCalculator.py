import math

#code block for d units and d inputs
    #d values represent the width or depth of the component

#Choose which units the d values will be entered as
dUnits = input("Will d values be entered in mm or inches? ")

#input validation to ensure input is an option
while(dUnits != "mm" and dUnits != "millimeters" and dUnits != "inches"):
    print("You did not enter the specified units")
    dUnits = input("Will d values be entered in mm or inches? ")

#user enters values of d0, di, d which are saved as variables in the form of float
d0 = float(input("Enter value of d0: "))
di = float(input("Enter value of di: "))
d = float(input("Enter value of d: "))
dvalues = [d0,di,d]

#if the units are entered in millimeters, they are converted to inches for ease of calculation
    #one inch is equivalent to 25.4 mm 
if dUnits == "mm" or dUnits == "millimeters":
    for i in range(len(dvalues)):
        dvalues[i] = dvalues[i]/25.4

#code block for L units and L inputs
       #L represents the Length of the components

#choose which units the length values will be entered as
lUnits = input("Will L values be entered in inches or meters? ")

#input validation to ensure input is an option
while(lUnits != "m" and lUnits != "meters" and lUnits != "inches"):
    print("You did not enter the specified units")
    lUnits = input("Will L values be entered in inches or meters? ")

#user enters values of L1, L2, L3 which are saved as variables in the form of float  
l1 = float(input("Enter value of L1: "))
l2 = float(input("Enter value of L2: "))
l3 = float(input("Enter value of L3: "))
lvalues = [l1,l2,l3]

#if the units are in meters, this converts it to inches for ease of calculation
    #one inch is equivalent to 0.0254 meters
if lUnits == "m" or lUnits == "meters":
    for i in range(len(lvalues)):
        lvalues[i] = lvalues[i]/0.0254


#code block for E units and E imputs
            #E represents the elasticity coefficient

#user chooses which units they will enter E values as
eUnits = input("Will E values be entered in ksi or GPa? ")

#input validation to ensure input is an option
while(eUnits != "ksi" and eUnits != "GPa"):
    print("You did not enter the specified units")
    eUnits = input("Will E values be entered in ksi or GPa? ")

#user inputs the values of E1, E2, E3 which are saved as variables in the form of float 
e1 = float(input("Enter value of E1: "))
e2 = float(input("Enter value of E2: "))
e3 = float(input("Enter value of E3: "))
evalues = [e1,e2,e3]

#if the values are entered as GPa, they are converted to ksi for ease of calculation
    #one ksi is equiavelent 145.03773773 GPa
if eUnits == "GPa":
    for i in range(len(evalues)):
        evalues[i] = evalues[i]/145.03773773


#code block for Pc units and Pc input

#choose whether internal force Pc is entered as kips or kN
pUnits = input("Will Pc values be entered in kips or kN? ")

#input validation to ensure input is an option
while(pUnits != "kips" and pUnits != "kN"):
    print("You did not enter the specified units")
    pUnits = input("Will Pc values be entered in kips or kN? ")

#user inputs the value of Pc which is saved as a variable in the form of float
pc = float(input("Enter value of Pc: "))

#if values are entered as kN, they are converted to ksi for ease of calculation
    #one ksi is equivalent to 0.224808943 kN
if pUnits == "kN":
    pc = pc/0.224808943

#EQUATIONS

#area equations
    #A1 expands in a linear fashion, and thus must be linearly interpolated. The other areas are only subject to the formula of cylindrical prisms, which is pi/4 (d^2)
A1 = (math.pi/4) * (pow(d0,2) - pow(di,2))
    #A2 is cylindrical, and is dependant on dimension 'd'
A2 = (math.pi/4) * pow(d,2)
    #A3 is the same as A2, because the 'd' value is constant throughout components 2 and 3
A3 = A2

#f equations
    #f is the flexibility coefficient, and is found by dividing the length by the product of the area and elasticity coefficent
f1 = l1/(A1 * e1)
f2 = l2/(A2 * e2)
f3 = l3/(A3 * e3)

#Force equations
    #Force equations are found through making a Free Body Diagram and writing force equilibrium equations
F2 = (f3 * pc)/(f1 + f2 + f3)
F1 = F2
F3 = F2 - pc

#displacement equations
uB = f1 * F1
uC = f3 * F3

#stress equations
stress1 = F1/A1
stress2 = F2/A2
stress3 = F3/A3
stressValues = [stress1,stress2,stress3]

#The displacements are displayed in inches and in mm because these are the outputs of displacement in parts (a) and (b)
print("Final displacement uB is ", uB, " in inches and ", uB*25.4, " in mm.")
print("Final displacement uC is ", uC, " in inches and ", uC*25.4, " in mm.")

#The stresses are displayed in ksi and MPa for parts (a) and (b)'s output.
    #The output will display whether the stress is in tension or compression, depending on its positive or negative value
for i in range(len(stressValues)):
    if stressValues[i] > 0:
        print("Stress ", i+1, " is ", stressValues[i], " in ksi and ", stressValues[i]*0.145037737, " in MPa and is in tension.")
    elif stressValues[i] < 0:
        print("Stress ", i+1, " is ", stressValues[i], " in ksi and ", stressValues[i]*0.145037737, " in MPa and is in compression.")
