import random

class Universe:
    def __init__(self,rows:int,cols:int) -> None:
        self.rows = rows
        self.cols = cols
        self.sector = [['-'for x in range(cols)] for y in range(rows)]

    def print_universe(self) -> None:
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.sector[x][y], ' ', end='')
            print('')

    def configure_universe(self,k_prob:float=3.0,s_prob:float=0.8, b_prob:float=0.4,w_prob:float=0.2) -> None:
        for x in range(self.rows):
            for y in range(self.cols):
                prob = (random.randint(1,1000))/10
                # print(prob)
                if prob <= k_prob:
                    self.sector[x][y] = Klingon()
                elif prob <= k_prob+s_prob:
                    self.sector[x][y] = SpaceStation()
                elif prob <= k_prob+s_prob+b_prob:
                    self.sector[x][y] = Blackhole()
                elif prob <= k_prob+s_prob+b_prob+w_prob:
                    self.sector[x][y] = Wormhole()

    def __repr__(self) -> str:
         return (f" Universe(rows:int,cols:int) -> None")
    
    def __str__(self) -> str:
         info1 = (f"Universe size is {self.rows} X {self.cols}, with {Klingon.num} Klingons, ") 
         info2 = (f"{SpaceStation.num} space stations, {Blackhole.num} black holes and {Wormhole.num} worm holes")
         return info1+info2

class StarShip:
    def __init__(self):
        self.energy = 1000
    pass

class CelestialBodie:
    pass

class Klingon(StarShip):
    num=0
    def __init__(self):
        Klingon.num+=1

    def __str__(self) -> str:
        return 'K'
    
class SpaceStation(StarShip):
    num=0
    def __init__(self):
        SpaceStation.num+=1

    def __str__(self) -> str:
        return 'S'

class Blackhole(CelestialBodie):
    num=0
    def __init__(self):
        Blackhole.num+=1

    def __str__(self) -> str:
        return 'B'

class Wormhole(CelestialBodie):
    num=0
    def __init__(self):
        Wormhole.num+=1

    def __str__(self) -> str:
        return 'W'


def main():

    u1 = Universe(10,10)
    u1.configure_universe()
    #print(repr(u1))
    #print(u1.__repr__())
    #print(u1)
    print('')
    u1.print_universe()
    print('')
    print("***************************************** STAR WARS! **********************************************")
    print('')
    print(u1)
    print('')
    print("***************************************************************************************************")

 

if __name__ == "__main__":
    main()
 
        
            