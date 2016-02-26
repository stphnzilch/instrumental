import pylab
from pylab import *
import matplotlib.pyplot as plt

from scipy import stats
import numpy as np

x = [ 0, 1, 10, 20, 30, 40, 50, 60]
A = [ 3.2352940037, 2.3529410936, 38.2352927712, 61.4705860706, 70.2941151717, 80.8823500929, 84.7058793701, 91.1764673775]
B = [ 2.6470587303, 17.3529405654, 33.8235282207, 57.3529391568, 66.7647035313, 71.7647033552, 81.7647030031, 81.7647030031]
C = [ 2.3529410936, 2.0588234569, 13.5294112883, 31.1764694904, 47.352939509, 58.8235273403, 72.3529386286, 86.1764675536]
D = [ 2.941176367, 2.3529410936, 3.5294116404, 7.0588232808, 10.5882349213, 15.5882347452, 19.9999992957, 28.5294107601]










(m,b)=polyfit(x,A,1)
print b 
print m
yp = polyval([m,b],x)
slope= "y=", m, "x+", b
print "slope: ", slope
slope, intercept, r_value, p_value, std_err = stats.linregress(x,A)
print "r-squared:", r_value**2
#plot(x,yp, color= 'blue')
plot(x,A, color= 'blue', label="0%")
grid(True)


(m,b)=polyfit(x,B,1)
print b 
print m
yp = polyval([m,b],x)
slope= "y=", m, "x+", b
print "slope: ", slope
slope, intercept, r_value, p_value, std_err = stats.linregress(x,B)
print "r-squared:", r_value**2
#plot(x,yp, color ='red')
plot(x,B, color ='red', label="10%")
grid(True)


(m,b)=polyfit(x,C,1)
print b 
print m
yp = polyval([m,b],x)
slope= "y=", m, "x+", b
print "slope: ", slope
slope, intercept, r_value, p_value, std_err = stats.linregress(x,C)
print "r-squared:", r_value**2
#plot(x,yp, color= 'green')
plot(x,C, color= 'green', label="20%")
grid(True)

(m,b)=polyfit(x,D,1)
print b 
print m
yp = polyval([m,b],x)
slope= "y=", m, "x+", b
print "slope: ", slope
slope, intercept, r_value, p_value, std_err = stats.linregress(x,D)
print "r-squared:", r_value**2
#plot(x,yp, color= 'yellow' )
plot(x,D, color= 'yellow', label="40%")
grid(True)
xlabel("M% delivered")
ylabel('Time (Min)')
title('Disolution of Hand Pressed Asprin')
#text(0, 2, r'y=0.23x-0.06')
#text(0, 1.8, r'r-squared: 0.998')


plt.legend(loc='best')



show()


pylab.show()
