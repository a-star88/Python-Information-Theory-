import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def hsb_to_rgb(hue, saturation, brightness):
    h = hue / 360.0
    s = saturation / 100.0
    v = brightness / 100.0
    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i = i % 6
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    elif i == 5:
        r, g, b = v, p, q
    return r, g, b

screen_width = 100  #x
screen_height = 100 #y
screen_depth = 100  #z

saturation = np.linspace(0, 100, screen_width)  #x
brightness = np.linspace(0, 100, screen_height) #y
hue = np.linspace(0, 360, screen_depth)         #z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# main array
all_x_vals = []
all_y_vals = []
all_z_vals = []
all_colors = []

# sub array 1
x_vals, y_vals = np.meshgrid(np.arange(screen_width), np.arange(screen_height))
z_vals = np.full_like(x_vals, 50)
colors = np.zeros((screen_width, screen_height, 3))
for x in range(screen_width):
    for y in range(screen_height):
        r, g, b = hsb_to_rgb(hue[50], saturation[x], brightness[y])
        colors[x, y, :] = [r, g, b]

all_x_vals.append(x_vals.flatten())
all_y_vals.append(y_vals.flatten())
all_z_vals.append(z_vals.flatten())
all_colors.append(colors.reshape(-1, 3))

# sub array 2
x_vals, z_vals = np.meshgrid(np.arange(screen_width), np.arange(screen_depth))
y_vals = np.full_like(x_vals, 50)
colors = np.zeros((screen_width, screen_depth, 3))
for x in range(screen_width):
    for z in range(screen_depth):
        r, g, b = hsb_to_rgb(hue[z], saturation[x], brightness[50])
        colors[x, z, :] = [r, g, b]

all_x_vals.append(x_vals.flatten())
all_y_vals.append(y_vals.flatten())
all_z_vals.append(z_vals.flatten())
all_colors.append(colors.reshape(-1, 3))

# sub array 3
y_vals, z_vals = np.meshgrid(np.arange(screen_height), np.arange(screen_depth))
x_vals = np.full_like(y_vals, 50)
colors = np.zeros((screen_height, screen_depth, 3))
for y in range(screen_height):
    for z in range(screen_depth):
        r, g, b = hsb_to_rgb(hue[z], saturation[50], brightness[y])
        colors[y, z, :] = [r, g, b]

all_x_vals.append(x_vals.flatten())
all_y_vals.append(y_vals.flatten())
all_z_vals.append(z_vals.flatten())
all_colors.append(colors.reshape(-1, 3))

# final array
all_x_vals = np.concatenate(all_x_vals)
all_y_vals = np.concatenate(all_y_vals)
all_z_vals = np.concatenate(all_z_vals)
all_colors = np.concatenate(all_colors)

ax.scatter(all_x_vals, all_y_vals, all_z_vals, color=all_colors, marker='s')

ax.set_xlabel('Saturation')
ax.set_ylabel('Brightness')
ax.set_zlabel('Hue')
plt.show()
