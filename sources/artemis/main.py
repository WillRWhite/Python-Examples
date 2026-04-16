from plotmods.plotmods import *

# Artemis I full journey: speed is Km/s
#filename = r"data_files/Post_TLI_Orion_AsFlown_20221213_EPH_OEM.asc"

# Artemis II full joureny: speed is Km/s
filename = r"data_files/Artemis_II_OEM_2026_04_09_Post-ICPS-Sep_to_EI.asc"

# Artemis II post RTC3 to entry interface: speed is ft/s
#filename = r"data_files/2026.04.10 - Post-RTC3 to EI"

x_coords, y_coords, z_coords = [], [], []
velocity, time = [], []

with open(filename, 'r') as f:
    t = 0 # Using equal time intervals. This is not very accurate need to improve
    for line in f:
        line = line.strip()
        # Only process lines that start with a year (e.g., '2026')
        if not line or not line[0].isdigit():
            continue
        
        parts = line.split()
        if len(parts) >= 4:
            # index 1, 2, 3 are X, Y, Z coordinates
            x_coords.append(float(parts[1]))
            y_coords.append(float(parts[2]))
            z_coords.append(float(parts[3]))

            x_velocity = float(parts[4])
            y_velocity = float(parts[5])
            z_velocity = float(parts[6])
            # Resultant velocity
            velocity.append(np.sqrt(x_velocity**2 + y_velocity**2 + z_velocity**2))
            time.append(t)
        t+=1 # Using equal time intervals. This is not very accurate need to improve

plot_velocity(time,velocity)
plt.show()

plot_trajectory(x_coords, y_coords, z_coords)
plt.show()

print(f"Max v = {max(velocity)}, min v = {min(velocity)} average v = {sum(velocity)/len(velocity)}")











"""
# Set up the 3D plot
fig = plt.figure(figsize=(12, 9)) # (10,8)
ax = fig.add_subplot(111, projection='3d')

# Plot the Orion trajectory
ax.plot(x_coords, y_coords, z_coords, label='Orion Path', color='cyan', linewidth=2)

# Optional: Add Earth at (0,0,0) for scale (Radius ~6371 km)
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
earth_x = 6371 * np.cos(u) * np.sin(v)
earth_y = 6371 * np.sin(u) * np.sin(v)
earth_z = 6371 * np.cos(v)
ax.plot_wireframe(earth_x, earth_y, earth_z, color='blue', alpha=0.2, label='Earth')

# Labels and formatting
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.set_title('Artemis Mission Trajectory (EME2000)')
ax.legend()

# Scale the axes equally
all_coords = np.array([x_coords, y_coords, z_coords])
max_range = (all_coords.max() - all_coords.min()) / 2.0
mid_x, mid_y, mid_z = all_coords.mean(axis=1)
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()

"""

