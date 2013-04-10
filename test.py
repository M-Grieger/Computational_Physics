# -*- coding: utf-8 -*-
"""
Created on Mon Apr 08 13:53:41 2013

@author: Marcel
"""

from numpy import *
from matplotlib import pyplot as plt

def wenn_Maus_geklickt(event):
    """Zeichnet Punkt an Mausposition."""
    plt.plot([event.xdata], [event.ydata], mfc='b', marker='o')
    plt.draw()

def wenn_Taste(event):
    """Wenn 's' gedrueckt: zeichne Sinus-Kurve."""
    if event.key == 'w':
        plt.plot(t, y, ls = '-', lw=1, c='r')
        plt.draw()
        
plt.figure(0)
plt.subplot(111, autoscale_on=False)
plt.axis([0, 2*pi, -1, 1])

t = linspace(0, 2*pi, 300)
y = sin(t)

plt.connect('button_press_event', wenn_Maus_geklickt)
plt.connect('key_press_event', wenn_Taste)
plt.show()