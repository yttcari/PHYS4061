import numpy as np
from raytracing_class import *
from envclass import *
from tqdm import tqdm



# Aspect ratio
if __name__ == '__main__':
    cam = camera(aspect_ratio=1, width=100, focal_length=1, viewport_height=2, centre=point(0,0,0), sample_ray_per_pixel=None, max_depth=3)

    world = hittable_list()
    #world.add(sphere(point(0, -100, -1), 100))
    #world.add(sphere(point(0, 0, -1), 0.5))

    cam.render(world)
    print(cam.pixel_du, cam.pixel_dv, cam.pixel_origin, cam.viewport_origin)

    #plot()

