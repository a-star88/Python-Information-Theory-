import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#plt.rcParams['toolbar'] = 'None'

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
    return r * 255, g * 255, b * 255

# User inputs for saturation and brightness
user_saturation = int(input("Enter a saturation value from 0 to 100: "))
user_brightness = int(input("Enter a brightness value from 0 to 100: "))

screen_width = 100
screen_height = 100
screen_depth = 360

saturation = np.linspace(0, 100, screen_width)
brightness = np.linspace(0, 100, screen_height)
hue = np.linspace(0, 360, screen_depth)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(hue_plane):
    ax.clear()

    # First plot: Slice at current hue_plane
    x_vals, y_vals = np.meshgrid(np.linspace(0, 100, screen_width), np.linspace(0, 100, screen_height))
    z_vals = np.full_like(x_vals, hue_plane)
    colors = np.zeros((x_vals.size, 3))
    for i, (x, y) in enumerate(zip(x_vals.flatten(), y_vals.flatten())):
        x_idx = min(int(round(x)), screen_width - 1)
        y_idx = min(int(round(y)), screen_height - 1)
        r, g, b = hsb_to_rgb(hue_plane, saturation[x_idx], brightness[y_idx])
        colors[i] = [r/255, g/255, b/255]

    ax.scatter(x_vals, y_vals, z_vals, color=colors, marker='.')

    ax.set_xlabel('Saturation')
    ax.set_ylabel('Brightness')
    ax.set_zlabel('Hue')

    # Update the inset with RGB rectangles
    r, g, b = hsb_to_rgb(hue_plane, user_saturation, user_brightness)

    inset_ax = inset_axes(ax, width="10%", height="5%", loc='upper left', borderpad=0)
    inset_ax.axis('off')

    inset_ax.add_patch(plt.Rectangle((0, 0), 1, 1.8, color=(r/255, 0, 0)))  
    inset_ax.add_patch(plt.Rectangle((1, 0), 1, 1.8, color=(0, g/255, 0)))  
    inset_ax.add_patch(plt.Rectangle((2, 0), 1, 1.8, color=(0, 0, b/255)))  

    inset_ax.text(4.5, 0.5, f'R: {int(r)} G: {int(g)} B: {int(b)}', ha='center', va='center', transform=inset_ax.transAxes)

    inset_ax.set_xlim(0, 4)
    inset_ax.set_ylim(0, 1.6)
    inset_ax.set_aspect('equal')

# Animation
ani = FuncAnimation(fig, update, frames=np.concatenate([np.arange(0, 361, 2), np.arange(359, -1, -2)]), interval=50)

plt.show()
