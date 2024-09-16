import random

class Universe():
    def __init__(self,rows:int,cols:int) -> None:
        self.rows = rows
        self.cols = cols
        self.sector = [['-'for x in range(cols)] for y in range(rows)]

    def print_universe(self) -> None:
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.sector[x][y], ' ', end='')
            print('')
    
    def configure_universe(self,k_prob:float=2.0,w_prob:float=2.0, ss_prob:float=2.0) -> None:
        #k_prob = (k_prob * self.rows * self.cols)/100
        #prob = random.randint(1,100)
        #k_prob = prob
        #self.k_prob = k_prob
        #print(self.k_prob)
        for x in range(self.rows):
            for y in range(self.cols):
                prob = (random.randint(1,1000)/100)
                if (prob <= k_prob):
                    self.sector[x][y] = 'K'
                elif (prob <= (k_prob + w_prob)):
                    self.sector[x][y] = 'W'
                elif (prob <= (k_prob + w_prob + ss_prob)):
                    self.sector[x][y] = 'S'

                
    def __repr__(self) -> str:
         return (f" Universe(rows:int,cols:int) -> None")
    
    def __str__(self) -> str:
         return (f"Universe size is {self.rows} X {self.cols}")

def main():

    u1 = Universe(10,10)
    u1.configure_universe(1,0,0)
    #print(repr(u1))
    #print(u1.__repr__())
    #print(u1)
    u1.print_universe()

 

if __name__ == "__main__":
    main()
 
        
            