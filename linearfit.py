import pylab
from pylab import *
import matplotlib.pyplot as plt

from scipy import stats
import numpy as np

x=[0, 1, 10, 20, 30, 40, 50, 60]
A=[0, -0.003, 0.119, 0.198, 0.228, 0.264, 0.277, 0.299]
B=[-0.002, -0.002, 0.048, 0.104, 0.184, 0.216, 0.233, 0.267]
C=[-0.003, -0.004, 0.035, 0.095, 0.15, 0.189, 0.235, 0.282]
D=[-0.001, -0.003, 0.001, 0.013, 0.025, 0.042, 0.057, 0.086]






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
xlabel('ppM')
ylabel('Abs')
title('Calibration Curve Phosphate')
text(0, 2, r'y=0.23x-0.06')
text(0, 1.8, r'r-squared: 0.998')


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
xlabel('ppM')
ylabel('Abs')
title('Calibration Curve Phosphate')
text(0, 2, r'y=0.23x-0.06')
text(0, 1.8, r'r-squared: 0.998')


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
xlabel('ppM')
ylabel('Abs')
title('Calibration Curve Phosphate')
text(0, 2, r'y=0.23x-0.06')
text(0, 1.8, r'r-squared: 0.998')

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
xlabel('Time')
ylabel('% delivered')
title('Disolution of Hand pressed Asprin')
#text(0, 2, r'y=0.23x-0.06')
#text(0, 1.8, r'r-squared: 0.998')


plt.legend(loc='best')



show()


pylab.show()
