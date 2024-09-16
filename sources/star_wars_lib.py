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
    
    # def configure_universe2(self,k_prob:float=3.0,w_prob:float=0.2, ss_prob:float=0.8) -> None:
    #     for x in range(self.rows):
    #         for y in range(self.cols):
    #             prob = (random.randint(1,1000)/10.0)
    #             if (prob <= k_prob):
    #                 self.sector[x][y] = 'K'
    #             #prob = (random.randint(1,1000)/10.0)
    #             if (prob <= w_prob):
    #                 self.sector[x][y] = 'W'
    #             #prob = (random.randint(1,1000)/10.0)
    #             if (prob <= ss_prob):
    #                 self.sector[x][y] = 'S'


    def configure_universe(self,k_prob:float=3.0,s_prob:float=0.8, b_prob:float=0.4,w_prob:float=0.2) -> None:
        self.num_k=0
        self.num_s=0
        self.num_b=0
        self.num_w=0
        for x in range(self.rows):
            for y in range(self.cols):
                prob = (random.randint(1,1000))/10
                # print(prob)
                if prob <= k_prob:
                    self.sector[x][y] = 'K'
                    self.num_k+=1
                elif prob <= k_prob+s_prob:
                    self.sector[x][y] = 'S'
                    self.num_s+=1
                elif prob <= k_prob+s_prob+b_prob:
                    self.sector[x][y] = 'B'
                    self.num_b+=1
                elif prob <= k_prob+s_prob+b_prob+w_prob:
                    self.sector[x][y] = 'W'
                    self.num_w+=1

    def __repr__(self) -> str:
         return (f" Universe(rows:int,cols:int) -> None")
    
    def __str__(self) -> str:
         info1 = (f"Universe size is {self.rows} X {self.cols}, with {self.num_k} Klingons, ") 
         info2 = (f"{self.num_s} space stations, {self.num_b} black holes and {self.num_w} worm holes")
         return info1+info2


def main():

    u1 = Universe(100,100)
    u1.configure_universe()
    #print(repr(u1))
    #print(u1.__repr__())
    #print(u1)
    #u1.print_universe()
    print('')
    print("***************************************** STAR WARS! **********************************************")
    print('')
    print(u1)
    print('')
    print("***************************************************************************************************")

 

if __name__ == "__main__":
    main()
 
        
            