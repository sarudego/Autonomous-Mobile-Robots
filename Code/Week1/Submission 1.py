
# coding: utf-8

# In[1]:

import packages.initialization
import pioneer3dx as p3dx
p3dx.init()


# In[ ]:




# In[ ]:




# In[2]:

def forward():
    # copy and paste your code here   
    target = 2        # target distance
    radius = 0.09765      # wheel radius
    initialEncoder = p3dx.leftEncoder
    distance = 0
    while distance < target:
        p3dx.move(2.5,2.5)
        angle = p3dx.leftEncoder - initialEncoder
        distance = angle * radius
    p3dx.stop()


# In[3]:

def turn():
    # copy and paste your code here
    target = 1.57
    #target = 0.7854      # target angle in radians
    r = 0.09765            # wheel radius
    L = 0.33          # axis length
    initialEncoder = p3dx.leftEncoder
    robotAngle = 0
    while robotAngle < target:
        p3dx.move(1.0,-1.0)
        wheelAngle = p3dx.leftEncoder - initialEncoder
        robotAngle = 2*(wheelAngle*r)/L
    p3dx.stop()


# In[4]:

print('Pose of the robot at the start')
p3dx.pose()
for _ in range(4):
    forward()
    turn()
print('Pose of the robot at the end')
p3dx.pose()


# In[7]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt   # WARNING: the first time, this import can take up to 30 seconds
x, y = p3dx.trajectory()          # because of font cache building, please be patient and wait
plt.plot(x,y);


# In[8]:

def move(V_robot, w_robot):
    w_r = (2*V_robot + L*w_robot)/2*r
    w_l = (2*V_robot - L*w_robot)/2*r
    p3dx.move(w_r, w_l)


# In[9]:

move(3, 3)


# In[ ]:



