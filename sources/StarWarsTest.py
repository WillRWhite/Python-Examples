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
    def __init__(self):
        self.life_support_date = 2000
        super().__init__()
        # Below is an alternative for running __init__ from parent class
        #StarShip.__init__(self)


print("")
# Instanciate a StarShip. This will never happen since it is a base class
ss = StarShip()

print(f"Ship details: x={ss._x}, y={ss._y}, energy={ss.energy}, torpedoes={ss.torpedoes}, phasers={ss.phasers}, shields={ss.sheilds} ")

# Manually change position of StarShip for testing
ss._x = 4
ss._y = 3
print(f"Ship details: x={ss._x}, y={ss._y}, energy={ss.energy}, torpedoes={ss.torpedoes}, phasers={ss.phasers}, shields={ss.sheilds} ")
print("")

# Instanciate The Enterprise
e = Enterprise()
# Print it's details
print(e._x, e._y, e.energy, e.torpedoes, e.sheilds, e.torpedoes, e.phasers,e.life_support_date)

# Manually change position of Enterprise for testing
e._x = 1
e._y = 2
print(e._x, e._y)

e.impulse_power(3,2)
print(e._x, e._y)


