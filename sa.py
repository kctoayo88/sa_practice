import numpy as np
import math

# Function
def inputfun(x, y):
    return math.cos(x)*math.sin(y)-(x/(y**2 + 1))

# Parameters
initT = 1000
minT = 1 
iterL = 100000
delta = 0.9 
k = 3

# Initialize
x = np.random.uniform(-1,2)
y = np.random.uniform(-1,1)
init_output = inputfun(x, y)

nowt = initT
init_x =x
init_y =y

print('-----init-----')
print('x, y:', init_x, init_y)
print('output:', init_output)

# SA
while nowt>minT:
    for i in np.arange(1, iterL, 1):
        funVal = inputfun(init_x, init_y)
        xnew = init_x + (2*np.random.rand()-1)
        ynew = init_y + (2*np.random.rand()-1) 
        if xnew>=-1 and xnew<=2 and ynew>=-1 and ynew<=1:
            funnew = inputfun(xnew, ynew)
            res = funnew - funVal
            if res<0:
                init_x = xnew
                init_y = ynew
            else:
                p = np.exp(-(res)/(k*nowt))
                r=np.random.uniform(0,1)
                if r<p:
                    init_x = xnew
                    init_y = ynew
    nowt = nowt * delta

print('------SA------')
print('x, y：', init_x, init_y)
print('output：', inputfun(init_x, init_y))