
# coding: utf-8

# <img align="right" src="img/wandering.png" />
# # Wandering
# 
# A simple wandering behavior can be achieved by the combination of the previously coded exercises: 
# 
#     repeat forever
#       move forward until an obstacle is detected
#       turn either left or right for free space
#       
# Instead of starting from scratch, you will reuse the code in two Python functions, which can be called from inside the main loop.

# In[265]:

import packages.initialization
import pioneer3dx as p3dx
p3dx.init()


# First, you need to copy and paste the code inside the following functions:

# In[266]:

def forward():
    min_dist = 1.5
    sensor3 = p3dx.distance[3]
    sensor4 = p3dx.distance[4]
    while sensor3 > min_dist and sensor4 > min_dist:
        if sensor3 > 1 and sensor4 > 1:
            speed = 5
        else:
            speed = 1
        p3dx.move(speed,speed)
        sensor3 = p3dx.distance[3]
        sensor4 = p3dx.distance[4]
p3dx.stop()


# In[267]:

# Note: in the first lap, the robot goes crazy and the second corner during a few seconds, next times works fine
def turn():
    min_dist = 1.2
    lMin = min(p3dx.distance[0:2])
    rMin = min(p3dx.distance[6:])
    sensor3 = p3dx.distance[3]
    sensor4 = p3dx.distance[4]
    if lMin > rMin:
        while sensor3 < min_dist and sensor4 < min_dist:
            p3dx.move(-1.5,1.5)
            sensor3 = p3dx.distance[3]
            sensor4 = p3dx.distance[4]
    else:
        while sensor3 < min_dist and sensor4 < min_dist:
            p3dx.move(1.5,-1.5)
            sensor3 = p3dx.distance[3]
            sensor4 = p3dx.distance[4]     
p3dx.stop()



# <img align="right" src="img/interrupt.png" />
# Finally, you should run the main loop in the following cell.
# 
# The execution can be stopped at any time by pressing the *interrupt kernel* button.

# In[268]:

try:
    while True:
        forward()
        turn()
except KeyboardInterrupt:
    p3dx.stop()


# The resulting trajectory can be plotted.

# In[148]:

get_ipython().magic(u'matplotlib inline')
import trajectory


# In[149]:

trajectory.plot()


# In[66]:

for i in range (8):
    print("Sensor %d is %.3f"% (i, p3dx.distance[i]))
lMin = min(p3dx.distance[0:3])
rMin = min(p3dx.distance[5:])
print(lMin)
print(rMin)


# Next application: [wall following](Wall%20Following.ipynb).

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
# 
