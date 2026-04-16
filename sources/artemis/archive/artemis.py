import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_artemis_trajectory(filename):
    x_coords, y_coords, z_coords = [], [], []

    # Read the OEM file
    with open(filename, 'r') as f:
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
    ax.set_title('Artemis II Mission Trajectory (EME2000)')
    ax.legend()
    
    # Scale the axes equally
    all_coords = np.array([x_coords, y_coords, z_coords])
    max_range = (all_coords.max() - all_coords.min()) / 2.0
    mid_x, mid_y, mid_z = all_coords.mean(axis=1)
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    plt.show()

# Replace with your actual filename
plot_artemis_trajectory('Artemis_II_OEM_2026_04_09_Post-ICPS-Sep_to_EI.asc')
