# Star Treck

# To-do:
# def ins()
#_Date
# need to sort out issue when Enterprise is at edge of universe


#Modules
import random
import time

# Game parametrs (constants:- should not be programtiacally modified)
universeSize = 60           # Universe size is a square (60)
Kprob=65                    # Probability of Universe cord having a Klingon (20)
Sprob=15                    # Probability of Universe cord having a space station (8)
Wprob=5                     # Probability of Universe cord having a worm hole (5)
srsRange = 3                # Short range scan range
starDate = 2000

# Variable initilisation
K_inUniverse = 0;           # Number of Klingons in universe
S_inUniverse = 0;	    # Space Stations in universe

# Global variables initilisation

# Initial status flags
shieldEnergy = 0                  # Maximum = 99
phaserEnergy = 0                  # Maxumul = 50


# Functions

# Clear screen
def clears():
    for i in range(60):
        print("")
    return

# Print lines
def lines(nl):
    for i in range(nl):
        print("")
    return

def energiseAnotation():
    for i in range(10):
        print(".", end="")
        time.sleep(0.25)
        i +=i
    time.sleep(2)

# Return a random number between 0 and 100
def rand(n):
    return random.randint(0,n)

# Short range scan with no print to get sector stats simular to srs but no display
# ssx, ssy :- Short Range Scan cords
def srs_noprint():
    global ex, ey
    K_inSector = 0;
    S_inSector = 0;
    W_inSector = 0;

    for ssx in range(ex-srsRange, ex+srsRange):
       for ssy in range(ey-srsRange, ey+srsRange):
          # To-do need to sort out issue when Enterprise is at edge of universe
          #  if ( ssx>0 and ssx<universeSize and ssy>0 and ssy<universeSize):
                if (Universe[ssx][ssy] == "K"):
                    K_inSector +=1
                elif (Universe[ssx][ssy] == "S"):
                    S_inSector +=1
                elif (Universe[ssx][ssy] == "W"):
                    W_inSector +=1
    return

# Short range scan
# ssx, ssy :- Short Range Scan cords
def srs():
    global energy, ex, ey
    K_inSector = 0;
    S_inSector = 0;
    W_inSector = 0;
    energy -=1

    if srsFlag <=0:
        clears()
        print("Short Range Scan not available")
        return
    else:
        clears()
        print(" "*12 + "8" + " "*(srsRange+3) + "  1" + " "*(srsRange+3) + "  2")
        for ssx in range(ex-srsRange, ex+srsRange+1):
            if ssx==ex:
                print(" "*12 + "7 ", end=" ")
            else:
                print(" "*14, end =" ")

            for ssy in range(ey-srsRange, ey+srsRange+1):
                if ssx<0 or ssx > universeSize-1:
                    print("  ", end =" ")
                elif ssy<0 or ssy > universeSize-1:
                    print("  ", end =" ")
                else:
                    print(Universe[ssx][ssy], end=" ")
                    if (Universe[ssx][ssy] == "K"):
                        K_inSector +=1
                    if (Universe[ssx][ssy] == "S"):
                        S_inSector +=1
                    if (Universe[ssx][ssy] == "W"):
                        W_inSector +=1
                if ssy==ey+srsRange and ssx==ex:
                    print(" 3", end=" ")
            print("")
        print(" "*12 + "6" + " "*(srsRange+3) + "  5" + " "*(srsRange+3) + "  4")
    return

def lrs():
    global energy
    if lrsFlag <= 0:
        clears()
        print("Long Range Scan unavilable.")
        return
    energy -= 3
    return

def impulse(direction, power):
    global ex, ey
    global K_inUniverse

    Universe[ex][ey] = "-"
    eOx = ex    # Store original position of Enterprise, so we can return if necessary
    eOy = ey
    if (direction < 1 or direction > 8):
        print("Direction value out of range")
    elif  (power < 1 or power > 3):
        print("Power value out of range")
    else:
        if direction == 1:
            ex = ex - power
            ey = ey
        elif direction == 2:
            ex = ex - power
            ey = ey + power
        elif direction == 3:
            ex = ex
            ey = ey + power
        elif direction == 4:
            ex = ex + power
            ey = ey + power
        elif direction == 5:
            ex = ex + power
            ey = ey
        elif direction == 6:
            ex = ex + power
            ey = ey - power
        elif direction == 7:
            ex = ex
            ey = ey - power
        elif direction == 8:
            ex = ex - power
            ey = ey - power
        else:
            #Should never get here
            print("Toto, this shue aint Kansus")

    if Universe[ex][ey] == "K":
        print("You have collided with a Klingon and suffered damage")
        K_inUniverse -= 1
        # To-do: Add damage




    Universe[ex][ey] = "E"
    #return




# Status report
def strpt():
    global srsFlag
    global lrsFlag
    global squadFlag
    global phaserFlag
    global ptFlag
    global warpFlag
    global impulseFlag
    global shieldEnergy
    global phaserEnergy

    srs_noprint()

    print("Status Report: STAR DATE: " + str(starDate) + ". Life support systems available until: " + str(max_starDate))
    print("--------------------------------------------------------------------------")
    print("Position:          " + str(ex) +":" + str(ey))
    print("Energy:            " + str(energy))
    print("Shields:           " + str(shieldEnergy))
    print("Phasers:           " + str(phaserEnergy))
    print("Photon torpedoes:  " + str(pt))

    if (srsFlag > 0):
        print("SRS operational")
    else:
        print("SRS unavailable")
    if (lrsFlag > 0):
        print("LRS operational")
    else:
        printf("LRS unavailable")
    if (squadFlag > 0):
        print("Save Quadrant operational")
    else:
        print("Save Quadrant unavailable")
    if (phaserFlag > 0):
        print("Phasers operational")
    else:
        print("Phasers unavailable")
    if (ptFlag > 0):
        print("Photon Torpedoes operational")
    else:
        print("Photon Torpedoes unavailable")
    if (warpFlag > 0):
        print("Warp power available");
    else:
        print("Warp power unavailable");
    if (impulseFlag > 0):
        print("Impulse power available");
    else:
        print("Impulse power unavailable");
    print("")

    #print("Klingons in sector: " + str(K_inSector))
    print("Klingons in universe: " + str(K_inUniverse))
    print("Space Stations in universe: " + str(S_inUniverse))
    #printf("Saved Quadrants: Q0: K=%2d S=%2d W=%2d   Q1: K=%2d S=%2d W=%2d\n", ssK[0], ssS[0], ssW[0], ssK[1], ssS[1], ssW[1]);
    #printf("                 Q2: K=%2d S=%2d W=%2d   Q3: K=%2d S=%2d W=%2d\n\n", ssK[2], ssS[2], ssW[2], ssK[3], ssS[3], ssW[3]);
    print("")


# Game introduction
def intro():
    clears()
    lines(8)
    print("\t\t\t * * * * * * * * * * *  *")
    print("\t\t\t *    **************    *")
    print("\t\t\t *    * STAR TRECK *    *")
    print("\t\t\t *    **************    *")
    print("\t\t\t *                      *")
    print("\t\t\t * Version 1.0          *")
    print("\t\t\t * By William White     *")
    print("\t\t\t * * * * * * * * * * *  *")
    lines(8)
    print("To list instrictions at any time type 'ins' at the command prompt.");
    print("Type <RETURN> to continue");
    input()



# ********************************************************************************
#                                 Main Program
# ********************************************************************************


# Create a universe of size "universeSize" with a random selection of
# Klingons (K), space stations (S) and worm holes (W)

#First initilise the universe so each co-ordinate is empty (-)
Universe = [["-" for x in range(universeSize)] for y in range(universeSize)]

#Populate the universe with Klingons, space stations and worm holes
for ux in range(0, universeSize):
    for uy in range(0, universeSize):
        #ran = rand_100()
        if rand(1000) < Kprob:
            Universe[ux][uy] = "K"
            K_inUniverse += 1
        elif rand(1000) < Sprob:
            Universe[ux][uy] = "S"
            S_inUniverse += 1
        elif rand(1000) < Wprob:
            Universe[ux][uy] = "W"
        #else:
        #    Universe[ux][uy] = "-"

# Place the Star Ship Enterprise somewhere in the universe. It must never
# be closer to the edge by less than one short range scan.
ex = random.randint(srsRange, universeSize-srsRange)
ey = random.randint(srsRange, universeSize-srsRange)
#ex = 0
#ey = 0

# decrement K/S count in case the Enterprise removes one
if Universe[ex][ey] == "K":
    K_inUniverse -= 1
if Universe[ex][ey] == "S":
    S_inUniverse -= 1

Universe[ex][ey] = "E"

# max_energy is more comples than this. See original C code
max_starDate = K_inUniverse * 18

max_pt = int(K_inUniverse/15)
pt = max_pt

max_energy = (4 * universeSize)
energy = max_energy

canDockDate = starDate

intro()
clears()
#ins()
strpt()

command=" "
while command != "ex":

    if (starDate > max_starDate):
        clears()
        print("\nYou have run out of time. Current star date is: " + str(starDate))
        print("You should have been finished by: " + str(max_starDate))
        break

    if (energy <= 0):
        clears()
        print("\nNo energy available")
        break

    print("Commands: srs, lrs, imp, wrp, wrq, sq, phr, pht, es, ep, str, ins, rep, help, ex.");
    command=input("Input command: ")
    if command=="srs":
        clears()
        srs()
    elif command=="lrs":
        clears()
        lrs()
    elif command=="imp":
        pd=input("Input [[Direction(1-8)][Power(1-3)]: ")
        impulsePower=int(pd[0])
        impulseDirection=int(pd[1])
        impulse(impulsePower, impulseDirection)
        #print("PD = " + str(p) + str(d))
        starDate = starDate + impulsePower
    elif command=="wrp":
        pd=input("Input [Power(0-9)][Direction(1-8)]: ")
        warpPower=int(pd[0])
        warpDirection=int(pd[1])
        starDate = starDate + 1
    elif command=="str":
        clears()
        strpt()
    elif command == "es":
        print("Input Energy: ", end = "")
        e = int(input())
        energy = energy - e
        shieldEnergy = shieldEnergy + e
        print("Energising shields ", end="")
        energiseAnotation()
        if shieldEnergy > 99:
            energy = energy + shieldEnergy - 99
            shieldEnergy = 99
            print(" Shields fully energied")
        else:
            print("Shield energised to " + str(shieldEnergy))
        time.sleep(2.5)
        clears()
        strpt()
    elif command == "ep":
        print("Input Energy: ", end = "")
        e = int(input())
        energy = energy - e
        phaserEnergy = phaserEnergy + e
        print("Energising phasers ", end="")
        energiseAnotation()
        if phaserEnergy > 50:
            energy = energy + phaserEnergy - 50
            phaserEnergy = 50
            print(" Phasers fully energied")
        else:
            print("Phasers energised to " + str(phaserEnergy))
        time.sleep(2.5)
        clears()
        strpt()




    else:
        clears()
        print("srs    	- Short Range Scan.")
        print("lrs    	- Long Range Scan.")
        print("imp 	- Impulse Power.")
        print("wrp	- Warp Power ( 2 for one sector move, 0 = hyoperspace ).")
        print("wrq	- Warp to saved quadrant.")
        print("sq	- Save Quadrant.")
        print("phr	- Phasers.")
        print("pht	- Photon Torpedoes.")
        print("es	- Energise Shields ( Max 100 ).")
        print("ep	- Energise Phasers ( Max 100 ).")
        print("str    	- Status Report.")
        print("sq	- Save Quadrant.")
        print("save	- Save game (note: only one game can be saved).")
        print("load	- Load game.")
        print("help   	- Help.")
        print("ins	- Print full instructions.")
        print("ex     	- End Game.\n")
        print("A 0 used in any command parameter (except Warp power 0 which")
        print("represents Warp Factor 10) results in the command being aborted")
        lines(1)





print("Gane Over")








