import numpy as np
from tqdm import tqdm
from raytracing_class import *
import cv2
import matplotlib.pyplot as plt

def render_object_color(ray, world):

    t_interval = interval(0, np.inf)

    hit_bool, rec = world.hit(ray, t_interval)
    if hit_bool:
        return 0.5 * (rec.n.vec + 1)
    else:
        unit_dir = to_vector(ray.dir).unit_vector()
        a = 0.5 * (unit_dir.y + 1)
        return (1 - a) * color(1, 1, 1).rgb + a * color(0.5, 0.7, 1).rgb

class camera:
    def __init__(self, aspect_ratio, width, focal_length, viewport_height, centre, sample_ray_per_pixel=None):
        self.aspect_ratio = aspect_ratio
        self.width = width

        height = round(width / aspect_ratio)
        self.height = height

        self.focal_length = focal_length 
        self.viewport_height = viewport_height

        viewport_width = viewport_height * width / round(width / aspect_ratio)
        self.viewport_width = viewport_width
        self.centre = centre

        viewport_u = np.array([viewport_width, 0, 0])
        viewport_v = np.array([0, -viewport_height, 0])

        pixel_du = viewport_u / width
        pixel_dv = viewport_v / height
        self.pixel_du = pixel_du
        self.pixel_dv = pixel_dv

        # Setting up the scene
        viewport_origin = centre.point - np.array([0, 0, focal_length]) - viewport_u / 2 - viewport_v / 2
        self.viewport_origin = viewport_origin
        self.pixel_origin = viewport_origin + 0.5 * (pixel_du + pixel_dv)

        # Antialiasing
        self.sample_ray_per_pixel = sample_ray_per_pixel
        

    def render(self, world):
        print(f"resolution: {self.width} * {self.height}")

        # Rendering
        f = open("image.ppm", "w")

        f.write("P3\n")
        f.write(f"{self.width} {self.height}\n")
        f.write("255\n")

        for j in tqdm(range(self.height)):
            for i in range(self.width):
                
                pixel_color = color(0, 0, 0).rgb
                if self.sample_ray_per_pixel is not None:
                    for sample_ray in range(self.sample_ray_per_pixel):
                        r = self.get_ray(i, j)
        
                        pixel_color = render_object_color(r, world) + pixel_color
                    pixel_color /= self.sample_ray_per_pixel
                else:
                    pixel_sample = self.pixel_origin + i * self.pixel_du + j * self.pixel_dv
                    r = ray(self.centre, to_vector(pixel_sample - self.centre.point))
                    pixel_color = render_object_color(r, world) + pixel_color
            
                write_color(f, pixel_color)

        f.close()
        plot()

    
    def get_ray(self, i, j):
        # for x, y elements of offset is [-0.5, 0.5]
        offset = vector(np.random.rand()-0.5, np.random.rand()-0.5, 0)

        pixel_sample = self.pixel_origin + (i + offset.x) * self.pixel_du + (j + offset.y) * self.pixel_dv
        r = ray(self.centre, to_vector(pixel_sample - self.centre.point))

        return r
    


def plot(image_path='image.ppm', customization=None, **kwargs):
    """
    plot the ppm image as plt.imshow()
    customization is a function that allow external customization
    """
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img, **kwargs)

    if customization is not None:
        customization()
        exit(0)
    
    plt.show()