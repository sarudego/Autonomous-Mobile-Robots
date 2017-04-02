
# coding: utf-8

# ## Complete Manipulation Task
# 
# Let's put everything together for the autonomous execution of the whole task.

# In[ ]:

import packages.initialization
import pioneer3dx as p3dx
p3dx.init()
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt


# ### Helper functions

# In[ ]:

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


# In[ ]:




# In[ ]:

def is_blob_centered():
    area, cx, cy = color_blob()
    if area > 0 and cx >= 70 and cx < 75:
        return True
    else:
        return False


# In[ ]:

def is_blob_close():
    area, cx, cy = color_blob()
    if area > 0 and cy >= 90:
        return True
    else:
        return False


# ### Search ball
# 
# Copy and paste the necessary code from previous notebooks for these subtasks:
# 
# * locate ball
# * approach to the ball
# * pick the ball

# In[ ]:

lower = numpy.array([110, 100, 100])
upper = numpy.array([130, 255, 255])




# In[ ]:

p3dx.gripper(0.05,0.1)
p3dx.tilt(-0.35)


# In[ ]:

while not is_blob_centered():
    p3dx.move(-0.5,0.5)
p3dx.stop()
plt.imshow(p3dx.image)
print('Area: %d, cx: %d, cy: %d' % color_blob())


# In[ ]:

while not is_blob_close():
    p3dx.move(1.0,1.0)
p3dx.stop()
plt.imshow(p3dx.image);


# In[ ]:

p3dx.tilt(-0.47)
while not is_blob_centered():
    p3dx.move(-0.5,0.5)
p3dx.stop()
while not is_blob_close():
    p3dx.move(1.0,1.0)
p3dx.stop()
plt.imshow(p3dx.image);


# In[ ]:

p3dx.gripper(0.05,0.0)
p3dx.sleep(2)
p3dx.gripper(-0.05,0.0)
plt.imshow(p3dx.image);


# In[ ]:




# ### Search target
# 
# Same for the target:
# 
# * locate target
# * approach to the target
# * release the ball

# In[ ]:

lower = numpy.array([ 0, 100, 100])
upper = numpy.array([ 10, 255, 255])


# In[ ]:

p3dx.tilt(-0.37)
plt.imshow(p3dx.image);


# In[ ]:

while not is_blob_centered():
    p3dx.move(0.3,-0.3)
p3dx.stop()


# In[ ]:




# In[ ]:

p3dx.tilt(-0.47)
while not is_blob_close():
    p3dx.move(1.0,1.0)
p3dx.stop()


# In[ ]:

plt.imshow(p3dx.image);


# In[ ]:

p3dx.gripper(0.05,0.0)


# In[ ]:

p3dx.gripper(0.05,0.1)
p3dx.move(-1.0,-1.0)
p3dx.sleep(3)
p3dx.stop()


# If completed, congratulations! You have programmed an autonomous mobile manipulation task!

# ---
# #### Try-a-Bot: an open source guide for robot programming
# Developed by:
# [![Robotic Intelligence Lab @ UJI](img/logo/robinlab.png "Robotic Intelligence Lab @ UJI")](http://robinlab.uji.es)
# 
# Sponsored by:
# <table>
# <tr>
# <td style="border:1px solid #ffffff ;">
# <a href="http://www.ieee-ras.org"><img src="img/logo/ras.png"></a>
# </td>
# <td style="border:1px solid #ffffff ;">
# <a href="http://www.cyberbotics.com"><img src="img/logo/cyberbotics.png"></a>
# </td>
# <td style="border:1px solid #ffffff ;">
# <a href="http://www.theconstructsim.com"><img src="img/logo/theconstruct.png"></a>
# </td>
# </tr>
# </table>
# 
# Follow us:
# <table>
# <tr>
# <td style="border:1px solid #ffffff ;">
# <a href="https://www.facebook.com/RobotProgrammingNetwork"><img src="img/logo/facebook.png"></a>
# </td>
# <td style="border:1px solid #ffffff ;">
# <a href="https://www.youtube.com/user/robotprogrammingnet"><img src="img/logo/youtube.png"></a>
# </td>
# </tr>
# </table>
