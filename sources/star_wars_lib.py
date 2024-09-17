import random

############### Parent Class Definitions ###############

####################### Univewrse ######################
class Universe:
    rows = 30
    cols = 30
    e_x = 0
    e_y = 0

    # Initilise universe sector grid. Fill each sector with a '-'
    # indicating an empty sector
    
    @classmethod
    def __init__(cls):
        cls.sector = [['-' for x in range(cls.cols)] for y in range(cls.rows)]

    # Print the universe as a retuangular grid. Only practiclr for relatively small universes
    @classmethod
    def print_universe_grid(cls) -> None:
        for x in range(cls.rows):
            for y in range(cls.cols):
                print(cls.sector[x][y], ' ', end='')
            print('')

    # Populate the universe with Klingons, space stations, blackholes and Wormholes
    @classmethod
    def populate_universe(cls,k_prob:float=3.0,s_prob:float=0.8, b_prob:float=0.4,w_prob:float=0.2) -> None:
        # "_prob" arguments are an approximate percentage weighting for each object - Klingon, 
        # SpaceStations Blackholes and Wormholews for each sector in the universe
        for x in range(cls.rows):
            for y in range(cls.cols):
                prob = (random.randint(1,1000))/10
                if prob <= k_prob:
                    cls.sector[x][y] = Klingon()
                elif prob <= k_prob+s_prob:
                    cls.sector[x][y] = SpaceStation()
                elif prob <= k_prob+s_prob+b_prob:
                    cls.sector[x][y] = Blackhole()
                elif prob <= k_prob+s_prob+b_prob+w_prob:
                    cls.sector[x][y] = Wormhole()
                else:
                    cls.sector[x][y] = '-'

        # Now add the Enterprise in a firly central location. 
        # Just obliterate whatever is there
        cls.e_x = random.randint(8, Universe.rows-8)
        cls.e_y = random.randint(8, Universe.cols-8)
        cls.sector[cls.e_x][cls.e_y] = Enterprise()

    @classmethod
    def __repr__() -> str:
         return (f" Universe(rows:int,cols:int) -> None")
     
    # def __str__() -> str:
    #      info1 = (f"Universe size is {rows} X {cols}, with {Klingon.num} Klingons, ") 
    #      info2 = (f"{SpaceStation.num} space stations, {Blackhole.num} black holes and {Wormhole.num} worm holes\n")
    #      info3 = (f"Enterprise co-ordinates: {e_x}, {e_y}")
    #      return info1+info2+info3
    
    @classmethod
    def info(cls) -> str:
         info1 = (f"Universe size is {cls.rows} X {cls.cols}, with {Klingon.num} Klingons, ") 
         info2 = (f"{SpaceStation.num} space stations, {Blackhole.num} black holes and {Wormhole.num} worm holes\n")
         info3 = (f"Enterprise co-ordinates: {cls.e_x}, {cls.e_y}")
         return info1+info2+info3

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

    Universe()
    Universe.populate_universe()
    #Enterprise()
    # print(repr(u1))
    # print(u1.__repr__())
    # print(u1)
    # print('')
    Universe.print_universe_grid()
    #print(f"Enterprise co-ordinates: {Universe.e_x}, {Universe.e_y}")
    print()
    print('')
    print("***************************************** STAR WARS! **********************************************")
    print('')
    #print(Universe.__str__())
    print(Universe.info())
    print('')
    print("***************************************************************************************************")

 

if __name__ == "__main__":
    main()
 
        
            