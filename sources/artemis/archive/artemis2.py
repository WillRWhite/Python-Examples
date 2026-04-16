from math import sqrt
import matplotlib.pyplot as plt

def artimis_velocity(filename):
    #x_velocity, y_velocity, z_velocity = [], [], []
    velocity = []
    time = []

    # Read the OEM file
    with open(filename, 'r') as f:
        i = 0
        for line in f:
            line = line.strip()
            # Only process lines that start with a year (e.g., '2026')
            if not line or not line[0].isdigit():
                continue
            
            parts = line.split()
            if len(parts) >= 4:
                # index 4, 5, 6 are X, Y, Z velocity components
                x_velocity = float(parts[4])
                y_velocity = float(parts[5])
                z_velocity = float(parts[6])
                # Resultant velocity
                velocity.append(sqrt(x_velocity**2 + y_velocity**2 + z_velocity**2))
                time.append(i)
            i+=1
        
        return time, velocity

time, velocity = artimis_velocity("Artemis_II_OEM_2026_04_09_Post-ICPS-Sep_to_EI.asc")

print(max(velocity))

plt.plot(time,velocity)
plt.show()
