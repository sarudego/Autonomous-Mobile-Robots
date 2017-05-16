
# coding: utf-8

import packages.initialization
import pioneer3dx as p3dx
p3dx.init()
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt


# ### Helper functions

import cv2
import numpy
def color_blob():
    hsv = cv2.cvtColor(p3dx.image, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    M = cv2.moments(mask)
    area = M['m00']
    if area > 0:
        cx = int(M['m10']/area)
        cy = int(M['m01']/area)
    else:
        cx = None
        cy = None
    return area, cx, cy


def is_blob_centered():
    area, cx, cy = color_blob()
    if area > 0 and cx >= 70 and cx < 75:
        return True
    else:
        return False

def is_blob_close():
    area, cx, cy = color_blob()
    if area > 0 and cy >= 90:
        return True
    else:
        return False


# ### Search ball
lower = numpy.array([110, 100, 100])
upper = numpy.array([130, 255, 255])

p3dx.gripper(0.05,0.1)
p3dx.tilt(-0.35)


while not is_blob_centered():
    p3dx.move(-0.5,0.5)
p3dx.stop()
plt.imshow(p3dx.image)
print('Area: %d, cx: %d, cy: %d' % color_blob())


while not is_blob_close():
    p3dx.move(1.0,1.0)
p3dx.stop()
plt.imshow(p3dx.image);


p3dx.tilt(-0.47)
while not is_blob_centered():
    p3dx.move(-0.5,0.5)
p3dx.stop()
while not is_blob_close():
    p3dx.move(1.0,1.0)
p3dx.stop()
plt.imshow(p3dx.image);


p3dx.gripper(0.05,0.0)
p3dx.sleep(2)
p3dx.gripper(-0.05,0.0)
plt.imshow(p3dx.image);


# ### Search target
lower = numpy.array([ 0, 100, 100])
upper = numpy.array([ 10, 255, 255])


p3dx.tilt(-0.37)
plt.imshow(p3dx.image);


while not is_blob_centered():
    p3dx.move(0.3,-0.3)
p3dx.stop()


p3dx.tilt(-0.47)
while not is_blob_close():
    p3dx.move(1.0,1.0)
p3dx.stop()


plt.imshow(p3dx.image);


p3dx.gripper(0.05,0.0)


p3dx.gripper(0.05,0.1)
p3dx.move(-1.0,-1.0)
p3dx.sleep(3)
p3dx.stop()


