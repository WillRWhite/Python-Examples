import random

############### Parent Class Definitions ###############

####################### Univewrse ######################
class Universe:
    def __init__(self,rows:int,cols:int) -> None:
        self.rows = rows
        self.cols = cols
        # Initilise universe sector grid. Fill each sector with a '-'
        # indicating an empty sector
        self.sector = [['-'for x in range(cols)] for y in range(rows)]

    # Print the universe as a retuangular grid. Only practiclr for relatively small universes
    def print_grid(self) -> None:
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.sector[x][y], ' ', end='')
            print('')

    # Populate the universe with Klingons, space stations, blackholes and Wormholes
    def populate(self,k_prob:float=3.0,s_prob:float=0.8, b_prob:float=0.4,w_prob:float=0.2) -> None:
        # "_prob" arguments are an approximate percentage weighting for each object - Klingon, 
        # SpaceStations Blackholes and Wormholews for each sector in the universe
        for x in range(self.rows):
            for y in range(self.cols):
                prob = (random.randint(1,1000))/10
                if prob <= k_prob:
                    self.sector[x][y] = Klingon()
                elif prob <= k_prob+s_prob:
                    self.sector[x][y] = SpaceStation()
                elif prob <= k_prob+s_prob+b_prob:
                    self.sector[x][y] = Blackhole()
                elif prob <= k_prob+s_prob+b_prob+w_prob:
                    self.sector[x][y] = Wormhole()

        # Now add the Enterprise in a fairly central location. 
        # Just obliterate whatever is there
        universe_edge = int((self.rows+self.cols)/2*0.1)
        x = random.randint(universe_edge, self.rows-universe_edge)
        y = random.randint(universe_edge, self.cols-universe_edge)
        self.sector[x][y] = Enterprise()
        Enterprise.x = x
        Enterprise.y = y

    def srs(self):
        for x in range(Enterprise.x-5, Enterprise.x+6):
            for y in range(Enterprise.y-5, Enterprise.y+6):
                print(self.sector[x][y], ' ', end='')
            print('')


    def __repr__(self) -> str:
         return (f" Universe(rows:int,cols:int) -> None")
    
    def __str__(self) -> str:
         info1 = (f"Universe size is {self.rows} X {self.cols}, with {Klingon.num} Klingons, ") 
         info2 = (f"{SpaceStation.num} space stations, {Blackhole.num} black holes and {Wormhole.num} worm holes")
         return info1+info2

####################### StarShip #######################
class StarShip:
    def __init__(self):
        self.energy = 1000
    pass
#################### CelestialBodie ####################
class CelestialBodie:
    pass

################ Child Class Definitions ###############

######################## Klingon #######################
class Klingon(StarShip):
    num=0
    def __init__(self):
        Klingon.num+=1

    def __str__(self) -> str:
        return 'K'

##################### SpaceStation #####################   
class SpaceStation(StarShip):
    num=0
    def __init__(self):
        SpaceStation.num+=1

    def __str__(self) -> str:
        return 'S'
    
###################### Enterprise ######################
class Enterprise(StarShip):
    x = 0
    y = 0
    def srs(self,Universe):
        Universe.srs()


    

    
    def __str__(self) -> str:
        return 'E'
    
###################### Blackhole #######################  
class Blackhole(CelestialBodie):
    num=0
    def __init__(self):
        Blackhole.num+=1

    def __str__(self) -> str:
        return 'B'
    
###################### Wormkhole #######################  
class Wormhole(CelestialBodie):
    num=0
    def __init__(self):
        Wormhole.num+=1

    def __str__(self) -> str:
        return 'W'

####################################### Main ####################################  
def main():

############################### Initilise the Game ##############################

    # Create an empty universe
    universe = Universe(40,40)
    # Populate the universe with Star Ships and Celestial Bodie using default weightings
    universe.populate()
    # Add the Star Ship Enterprise somewhere in the middle of the universe
    enterprise = Enterprise()

    print(repr(universe))
    print(universe)
    print('')

    universe.print_grid()
    print('')
    print("***************************************** STAR WARS! **********************************************")
    print('')
    print(universe)
    print(f"Enterprose co-ordinates: {enterprise.x} {enterprise.y}")
    print('')
    print("***************************************************************************************************")
    #universe.srs()
    enterprise.srs(universe)
    print('')
    enterprise.srs(universe)
    print('')
    universe.srs()
    

 

if __name__ == "__main__":
    main()
 
        
            