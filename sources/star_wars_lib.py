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
    
    def __repr__(self) -> str:
        return (f"Universe(rows:int,cols:int) -> None")
    
    def __str__(self) -> str:
        return (f"Universe size is {self.rows} X {self.cols}")

def main():

    u1 = Universe(5,6)
    print(repr(u1))
    print(u1.__repr__())
    print(u1)
    u1.print_universe()
 

if __name__ == "__main__":
    main()
 
        
            