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
    def print_universe_grid(self) -> None:
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.sector[x][y], ' ', end='')
            print('')

    # Populate the universe with Klingons, space stations, blackholes and Wormholes
    def populate_universe(self,k_prob:float=3.0,s_prob:float=0.8, b_prob:float=0.4,w_prob:float=0.2) -> None:
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

        # Now add the Enterprise in a firly central location. 
        # Just obliterate whatever is there
        x = random.randint(8, self.rows-8)
        y = random.randint(8, self.cols-8)
        self.sector[x][y] = Enterprise()


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

######################## Main ##########################  
def main():

    u1 = Universe(20,20)
    u1.populate_universe()
    e = Enterprise()
    # print(repr(u1))
    # print(u1.__repr__())
    # print(u1)
    # print('')
    u1.print_universe_grid()
    print('')
    print("***************************************** STAR WARS! **********************************************")
    print('')
    print(u1)
    print('')
    print("***************************************************************************************************")

 

if __name__ == "__main__":
    main()
 
        
            