import subprocess
import cv2
import matplotlib.pyplot as plt
import time
"""
This python act as a wrapper for the real rendering c files
Also providing a instant view for the rendered image
$ python render.py
"""

start_time = time.time()
subprocess.call(['make'])
end_time = time.time()
print(f"Compile time used {end_time - start_time}")

start_time = time.time()
subprocess.call(['./bin/render'])
end_time = time.time()
print(f"Running time used {end_time - start_time}")

subprocess.call(['rm', '-r', './obj'])
end_time = time.time()


img = cv2.imread("image.ppm")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()