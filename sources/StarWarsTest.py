class SpaceVehicle():
    def __init__(self, vehicle_type:chr) -> None:
        self.vehicle_type = vehicle_type
        if vehicle_type != 'E' and  vehicle_type != 'K' and vehicle_type != 'S': 
            print(vehicle_type, "is not a valid space vehicle")
        else:
            print(vehicle_type, "created")

enterprise = SpaceVehicle("E")
k1 = SpaceVehicle("K")
ss1 = SpaceVehicle("S")
nasa = SpaceVehicle("A")
