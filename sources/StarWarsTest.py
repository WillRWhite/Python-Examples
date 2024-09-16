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
        self.torpedoes = 20
        self.sheilds = 10
        self.phasers = 5
    
    def add_torpedoes(self,num:int) -> None:
        self.torpedoes + num 

class Enterprise(StarShip):
    def __init__(self):
        self.life_support_date = 2000
        super().__init__()
        # Below is an alternative
        #StarShip.__init__(self)
 


ss = StarShip()
print(ss.sheilds, ss.torpedoes)

e = Enterprise()
print(e.sheilds, e.torpedoes, e.life_support_date)

