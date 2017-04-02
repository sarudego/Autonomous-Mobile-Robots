
# coding: utf-8

# ## Ball Picking Challenge
# 
# ### Part 2: Pick and Place
# 
# The aim is to program the robot for the second part of the challenge: pick up the balls and transport them to the corner. To do so, you need to reuse the abilities learnt in week 4; please feel free to reuse the code of those notebooks and exercises.

# In[76]:

import packages.initialization
import packages.pioneer3dx as p3dx
import time
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import cv2
import numpy 
p3dx.init()
time.sleep(2)


# In[77]:

lower_blue = numpy.array([100,  50,  50])
upper_blue = numpy.array([130, 255, 255])
lower_red = numpy.array([ 170, 100, 50])
upper_red = numpy.array([ 220, 255, 255])
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 5
detector = cv2.SimpleBlobDetector(params)


# In[78]:

def blue_balls():
    hsv = cv2.cvtColor(p3dx.image, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    reversemask = 255-mask
    keypoints = detector.detect(reversemask)
    l = []
    for i,kp in enumerate(keypoints):
        l.append((kp.size,) + kp.pt)
    l.sort(key=lambda tup: tup[0], reverse=True)
    return l


# In[79]:

def is_ball_centered():
    b = blue_balls()
    diametre = 0
    while not b:
        p3dx.move(-0.2,0.2)
        b = blue_balls()
    for ball in b:
        if ball[0] > diametre:
            diametre = ball[0]
            cx = b[0][1]
    if cx >= 70 and cx < 80:
        return True
    else:
        return False


# In[80]:

def is_ball_close():
    b = blue_balls()
    cx = 0
    cy = 0
    revers = 1
    diametre = 0
    while not b:
        p3dx.move(-0.1,0.1)
        b = blue_balls()
    for ball in b:
        if ball[2] > cy:
            diametre = ball[0]
            cy = ball[2]
            cx = ball[1]
    if cx > 90 or cx < 60:
        print 'ball not in the center'
        if cx > 80:
            revers = -1
        while not is_ball_centered():
            p3dx.move(-0.1 * revers,0.1 * revers)
    if cy + diametre/2 >= 80:
        return True
    else:
        return False


# In[81]:

def color_blob():
    hsv = cv2.cvtColor(p3dx.image, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    M = cv2.moments(mask)
    area = M['m00']
    if area > 0:
        cx = int(M['m10']/area)
        cy = int(M['m01']/area)
    else:
        cx = None
        cy = None
    return area, cx, cy


# In[82]:

def is_blob_centered():
    area, cx, cy = color_blob()
    if area > 0 and cx >= 70 and cx < 80:
        return True
    else:
        return False


# In[83]:

def is_blob_close():
    area, cx, cy = color_blob()
    if area > 0 and cy >= 70:
        return True
    else:
        return False


# In[84]:

def picking_ball():
    p3dx.tilt(-0.2)
    time.sleep(1)
    print 'centring the ball'
    while not is_ball_centered():
        p3dx.move(-0.5,0.5)
    p3dx.move(0,0)
    print 'going to the ball'
    while not is_ball_close():
        p3dx.move(2.0,2.0)
    p3dx.move(0.0,0.0)
    print 'openning the gripper'
    p3dx.tilt(-0.47)
    p3dx.gripper(0.05,1.0)
    time.sleep(1)
    print 'going to the ball slowly'
    while not is_ball_close():
        p3dx.move(0.5,0.5)
    print 'picking the ball'
    p3dx.move(0.5,0.5)
    time.sleep(3.5)
    p3dx.move(0,0)
    p3dx.gripper(0.05,0.0)
    time.sleep(1)
    p3dx.gripper(-0.05,0.0)
    time.sleep(1)


# In[85]:

def go_to_red():
    p3dx.tilt(-0.1)
    print 'finding the red area'
    while not is_blob_centered():
        p3dx.move(-0.5, 0.5)
    print 'going to the red area'
    while not is_blob_close():
        p3dx.move(2.0,2.0)
        area, cx = blue_ball_in_way()
        if area > 0:
            print "ball in the way!!"
            print cx
            avoid_ball(cx)
    p3dx.move(0.5, 0.5)
    p3dx.tilt(-0.22)
    time.sleep(1)
    print 'going to the red area slowly'
    while not is_blob_close():
        p3dx.move(0.5, 0.5)
    p3dx.move(0,0)


# In[86]:

def lose_ball():
    p3dx.gripper(0.05,0.0)
    time.sleep(1)
    p3dx.gripper(0.05,1.0)
    time.sleep(1)
    p3dx.move(-2,-2)
    time.sleep(2)
    p3dx.move(0,0)
    p3dx.tilt(-0.3)
    time.sleep(1)
    p3dx.move(-1.0,1.0)
    time.sleep(3)
    p3dx.move(-0.5,0.5)


# In[87]:

def check_ball():
    p3dx.tilt(-0.47)
    time.sleep(1)
    hsv = cv2.cvtColor(p3dx.image, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #print mask[70:80,70:80]
    return True if mask[70:80,70:80].any() > 0 else False


# In[88]:

def blue_ball_in_way():
    hsv = cv2.cvtColor(p3dx.image, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask[0:90, 0:150] = 0
    mask[90:100, 0:50] = 0
    mask[90:100, 100:150] = 0
    M = cv2.moments(mask)
    area = M['m00']
    if area > 0:
        cx = int(M['m10']/area)
    else:
        cx = None
    return area, cx


# In[89]:

def avoid_ball(cx):
    print "avoiding ball"
    p3dx.move(0.5, 0.5)
    time.sleep(8)
    if cx > 75:
        p3dx.move(-0.5, 0.5)
        time.sleep(4)
        p3dx.move(1.6, 0.7)
        time.sleep(9)
        while not is_blob_centered():
                p3dx.move(-0.5, 0.5)
    else:
        p3dx.move(0.5, -0.5)
        time.sleep(4)
        p3dx.move(0.7, 1.6)
        time.sleep(9)
        while not is_blob_centered():
                p3dx.move(0.5, -0.5)
    p3dx.move(0, 0)


# In[90]:

try:     
    transfared_ball = 0
    while transfared_ball < 5:
        while not check_ball():
            picking_ball()
        go_to_red()
        if check_ball():
            lose_ball()
            transfared_ball += 1
            print transfared_ball
    p3dx.move(0,0)
    print "FINALY DONE"
except KeyboardInterrupt:
    p3dx.stop()


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
