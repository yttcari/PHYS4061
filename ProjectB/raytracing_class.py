import numpy as np 

# Some useful functions
def to_vector(array):
    """
    Take in 3d numpy array, change it to vector object:
    """

    return vector(array[0], array[1], array[2])

def gradient_color(r):
    # r is a ray object
    ray = vector(r.dir[0], r.dir[1], r.dir[2])
    a = 0.5 * (ray.unit_vector().y + 1)

    start_color = color(1, 1, 1)
    end_color = color(0.5, 0.7, 1)

    final_color =  (1 - a) * start_color.rgb + a * end_color.rgb

    return final_color

def write_color(f, color):
    # color should be a 3d numpy array
    color = color * 255.9
    ir = int(np.clip(color[0], 0, 255))
    ig = int(np.clip(color[1], 0, 255))
    ib = int(np.clip(color[2], 0, 255))
    f.write(f"{ir} {ig} {ib}\n")

 
# Object

class interval:
    def __init__(self, min, max):
        self.max = max
        self.min = min
        self.size = max - min

    def ifcontain(self, x):
        return x < self.max and x < self.min
    
    def ifsurround(self, x):
        return x <= self.max and x <= self.min
    
    def bound(self, x):
        if x < self.min:
            return self.min
        elif x > self.max:
            return self.max
        else:
            return x

    
class color:
    """
    Stored rgb value as [0, 1]
    pixel_color is used to write color in ppm file
    """
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.rgb = np.array([r, g, b])

    def pixel_color(self):
        return [self.rgb[0] * 255.999, self.rgb[1] * 255.999, self.rgb[2] * 255.999]
    
class vector:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.vec = np.array([x, y, z])

    def length(self):
        return np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def unit_vector(self):
        len = self.length()
        return vector(self.x / len, self.y / len, self.z / len)
    
    def to_array(self):
        return np.array([self.x, self.y, self.z])

class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.point = np.array([x, y, z])

class ray:
    """
    origin: ray origin, should be in point class
    dir: direction of the ray, should be in vector class
    """
    def __init__(self, origin, dir):
        self.origin = origin.point
        self.dir = dir.vec

    def at(self, t):
        return to_vector(self.origin + t * self.dir)
    
class hit_record:
    def __init__(self, p, n, t):
        # point direction, from ray origin to t * d
        self.p = p
        # normal vector
        self.n = n
        # scalar
        self.t = t

    def set_face_normal(self, ray, outward_normal):
        """
        outward_normal should be a vector object
        """
        ray_normal_intersect = np.dot(ray.dir, outward_normal.vec)

        if ray_normal_intersect < 0:
            self.n = to_vector(-outward_normal.vec)
        else:
            self.n = outward_normal
    

class sphere:
    """
    centre: circumcentre of the sphere, should belong to point class
    """
    def __init__(self, centre, radius):
        self.centre = centre.point
        self.radius = radius

    def hit(self, ray, t_interval, rec):
        # displacement between ray origin and the sphere centre
        displacement = self.centre - ray.origin

        a = np.dot(ray.dir, ray.dir)
        b = np.dot(ray.dir, displacement)
        c = np.dot(displacement, displacement) - self.radius ** 2

        discriminant = b ** 2 - a * c
        if discriminant < 0:
            return False

        discriminant = np.sqrt(discriminant)

        root = (b - discriminant) / (2*a)
        if t_interval.ifsurround(root):
            return False
        else:
            root = (b + discriminant) / (2*a)
            if t_interval.ifsurround(root):
                return False
        rec.t = root
        rec.p = ray.at(rec.t)

        outward_normal = to_vector((rec.p.vec - self.centre) / self.radius)
        rec.n = outward_normal
        #rec.set_face_normal(ray, outward_normal)

        return True, rec
    
class hittable_list:
    """
    For storing all hittable object
    """
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)
    
    def clear(self):
        self.objects = []

    def hit(self, ray, t_interval):
        # whether the ray has hit an object
        hit_bool = False
        temp_rec = hit_record(0, 0, 0)

        for obj in self.objects:
            if obj.hit(ray, t_interval, temp_rec):
                hit_bool = True
                t_interval.max = temp_rec.t

        return hit_bool, temp_rec
    
