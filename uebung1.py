# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 07:27:06 2013

@author: Marcel
"""

from numpy import *                     # numpy operationen importieren
from matplotlib import pyplot as plt    # plot-Funktionen importieren

def get_start(event):                   # Startpos. via Mausklick
    it = 1001                           # Anzahl der Iterationen - 1
    K = 0.5                             # Festlegung des Parameters K
    phi = 1.*arange(it)                 # Array initialisieren mit Itera-
    p = 1.*arange(it)                   #  tionen
    phi[0] = event.xdata                # Startwert phi
    p[0] = event.ydata                  # Startwert p
    for i in range(1, it):              # Schleife von 1 bis it-1
        phi[i] = phi[i-1] + p[i-1]      # Berechnung der Standardabbildung phi
        phi[i] = phi[i] % (2.*pi)       # Realisierung period. RB f. phi
        p[i] = p[i-1] + K * sin(phi[i]) # Berechnung p
        p[i] = (p[i]+pi) % (2*pi) - pi  # Realisiserung period. RB f. p
    print phi, p                        # Ausgabe LÖSCHEN
    plt.plot(phi[0], p[0], marker='o')  # plotten des Startpunktes
    plt.plot(phi, p)                    # plotten der Iteration
    plt.draw()                          # zeichnen


plt.figure(0)
plt.title("Titel")
plt.xlabel("Phi")
plt.ylabel("P")
plt.plot()
plt.axis([0.0,2.0*pi,-pi,pi])
plt.connect('button_press_event', get_start)
plt.show()

## todo: zoommodus fehlerabfrage