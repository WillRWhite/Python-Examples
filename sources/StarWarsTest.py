# class SpaceVehicle():
#     def __init__(self, vehicle_type:chr) -> None:
#         # vehicle_type variable is only available in this --init_ method
#         # if we need to access in in another class method will need the
#         # "self" assignment below
#         self.vehicle_type = vehicle_type

#         match vehicle_type:
#             case 'E': vehicle_type_str = "Enterprise"
#             case 'K': vehicle_type_str = "Klingon"
#             case 'S': vehicle_type_str = "Space Station"
#             case _: vehicle_type_str = "Unknown vehicle"

#         if vehicle_type != 'E' and  vehicle_type != 'K' and vehicle_type != 'S': 
#             print(vehicle_type_str, "not valid")
#         else:
#             print(vehicle_type_str, "created")

# enterprise = SpaceVehicle('E')
# klingon1 = SpaceVehicle('K')
# space_station1 = SpaceVehicle('S')
# nasa = SpaceVehicle('A')

class StarShip():
    def __init__(self) -> None:
        self._x = 0
        self._y = 0
        self.energy:int = 1000
        self.torpedoes:int = 20
        self.phasers:int = 5
        self.sheilds:int = 10
         
    # Private Methods
    ###########################################################
    def _move(self,_x:int,_y:int):
        # Calculate new cordinates
        self._x = _x
        self._y = _y

    ###########################################################

    def impulse_power(self,power:int,dir:int):
        # Private function inherited from StarShip
        self._x = self._x + power
        self._y = self._y + dir
        self._move(self._x,self._y)
 
    
    def add_torpedoes(self,num:int) -> None:
        self.torpedoes + num 

class Enterprise(StarShip):
    def __init__(self, _universe:list):
        # If you happen to use the same list name for "univ" as you do in the
        # main program this may cause problems because thelist is effectively 
        # global?
        self._universe = _universe
        self.life_support_date = 2000
        super().__init__()
        # Below is an alternative for running __init__ from parent class
        #StarShip.__init__(self)

    # getter / setter methods
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def get_position(self):
        return(self._x, self._y)
    
    # @x.setter
    # def x(self, x:int):
    #     self._x = x

    # @y.setter
    # def y(self, y:int):
    #     self._y = y

    #@position.setter
    # Why is this not a setter - because it is a proper function which takes arguments
    def set_position(self,x:int, y:int):
        # First we need to replace the Enterprise's current position with empty space 
        self._universe[self._x][self._y] = '-'
        # Now assign the new co-ordinates for the enterprise and check valid and correct
        # with default if necessary
        self._x = x
        self._y = y
        if self._y < 0 or self._x < 0 or self._y >= len(self._universe[0]) or self._x >= len(self._universe[0]):
        #if (self._x >= len(self._universe) or self._x < 0 or self._y >= len(self._universe[0]) or self._y) < 0:
            print("You can't escape the universe")
            # Se default positions
            self._x = int(len(self._universe)/2)
            self._y = int(len(self._universe[0])/2)
        self._universe[self._x][self._y] = 'E'

def create_universe(rows:int=100,cols:int=100,k_prob:float=3.0,s_prob:float=0.8, b_prob:float=0.4,w_prob:float=0.2) -> list:
    #universe_dim = [rows,cols]
    # Create an empty universe of size rows x cols
    universe = [['-'for x in range(cols)] for y in range(rows)]
    return (universe)

def print_universe(universe):
    for y in range(len(universe[0])):
        for x in range(len(universe)):
            print(universe[x][y], end="  ")
        print("")


if __name__ == "__main__":

    ux = 9
    uy = 9
    universe = create_universe(ux,uy)
    #print(len(universe[0]))
    #print(len(universe))

    # Crerate an Enterprise in the universe
    e = Enterprise(universe)
    # Print the Enterprise's position
    print(e.get_position())

    # Set an new position for the Enterprise
    e.set_position(6,2)
    print(e.get_position())
    print_universe(universe)

    # Try to set a position outside of the universe
    e.set_position(6,100)
    print(e.get_position())
    print_universe(universe)

    e.set_position(100,6)
    print(e.get_position())
    print_universe(universe)








# print("")
# # Instanciate a StarShip. This will never happen since it is a base class
# ss = StarShip()

# print(f"Ship details: x={ss._x}, y={ss._y}, energy={ss.energy}, torpedoes={ss.torpedoes}, phasers={ss.phasers}, shields={ss.sheilds} ")

# # Manually change position of StarShip for testing
# ss._x = 4
# ss._y = 3
# print(f"Ship details: x={ss._x}, y={ss._y}, energy={ss.energy}, torpedoes={ss.torpedoes}, phasers={ss.phasers}, shields={ss.sheilds} ")
# print("")

# # Instanciate The Enterprise
# e = Enterprise()
# # Print it's details
# print(e._x, e._y, e.energy, e.torpedoes, e.sheilds, e.torpedoes, e.phasers,e.life_support_date)

# # Manually change position of Enterprise for testing
# e._x = 1
# e._y = 2
# print(e._x, e._y)

# e.impulse_power(3,2)
# print(e._x, e._y)


