import numpy as np
from raytracing_class import *
from envclass import *
from tqdm import tqdm

"""
TODO

- make video to show the effect of different sample_ray_per_pixel, including those that has no antialiasing

"""

# Aspect ratio
cam = camera(aspect_ratio=16/9, width=400, focal_length=1, viewport_height=2, centre=point(0,0,0), sample_ray_per_pixel=None)

world = hittable_list()

world.add(sphere(point(0, -100, -1), 100))
world.add(sphere(point(0, 0, -1), 0.5))

cam.render(world)

def show():
    plt.xlim(255, 280)
    plt.ylim(130, 95)

    plt.show()

plot(customization=show)

# 255,120 280, 95