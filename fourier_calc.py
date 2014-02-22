import numpy as np
from numpy import fft
from numpy.fft import rfft2
import csv
import matplotlib.pyplot as plt

# time = []
voltage = []

with open('HAMMERB_4.isf','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        # time.append(float(row[0]))
        voltage.append(float(row[1]))

voltage2 = np.array(voltage)
# time2 = np.array(time)
# print voltage2

something = np.fft.fft(a=voltage2)
freq = fft.fftfreq(voltage2.size,d=.0001)
plt.plot(freq, something)
plt.show()

# Plots shit.
# plt.plot(time)
# plt.show()

# f_trans = rfft2(a= , s=None, axis = )