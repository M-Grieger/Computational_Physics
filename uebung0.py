# -*- coding: utf-8 -*-
"""
Created on Tue Apr 09 12:36:48 2013

@author: Marcel
"""

from numpy import *                     # numpy operationen importieren
from matplotlib import pyplot as plt    # plot-Funktionen importieren

def spir(x0,y0):                        # Spirale zeichnen am Ort x0, y0
    t = linspace(0, 5, 3000)            # Definition des Parameters
    r  = (0.5)**t                       # 
    phi = 2.*pi*t                       # Darstellung der Spirale polar
    x = sin(phi)*r + x0                 #
    y = cos(phi)*r + y0                 # Transformation zu kartesisch
    plt.plot(x,y)                       # plotten und
    plt.draw()                          # zeichnen der Spirale

def wenn_Maus_geklickt(event):          # Verknüpfung von Mausklickevent und
                                        # Spirale zeichnen
    """Zeichnet Spirale an Mausposition."""
    spir([event.xdata], [event.ydata])  # Spirale bei Mausklick zeichnen

# Hauptprogramm

plt.subplot(111, aspect=1.0)
spir(0,0)
plt.connect('button_press_event', wenn_Maus_geklickt)
plt.show()