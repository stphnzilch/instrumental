import pylab
from pylab import *
import matplotlib.pyplot as plt

from scipy import stats
import numpy as np


x= [0, 160, 80, 40, 20, 117.06]
A= [0, 0.542, 0.242, 0.119, 0.059, 0.387]

(m,b)=polyfit(x,A,1)
print b 
print m
yp = polyval([m,b],x)
slope= "y=", m, "x+", b
print "slope: ", slope
slope, intercept, r_value, p_value, std_err = stats.linregress(x,A)
print "r-squared:", r_value**2
plot(x,yp, color= 'blue')
plot(x,A, color= 'blue', label="0%")
grid(True)
xlabel('ppM')
ylabel('Abs')
title('Calibration Curve Phosphate')
text(0, 2, r'y=0.23x-0.06')
text(0, 1.8, r'r-squared: 0.998')

plt.legend(loc='best')



show()


pylab.show()
