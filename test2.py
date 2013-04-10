# -*- coding: utf-8 -*-
"""
Created on Tue Apr 09 12:33:44 2013

@author: Marcel
"""

import numpy as N
import matplotlib.pyplot as P

angle = N.arange(0, 360, 10, dtype=float) * N.pi / 180.0
arbitrary_data = N.abs(N.sin(angle)) + 0.1 * (N.random.random_sample(size=angle.shape) - 0.5)

P.clf()
P.polar(angle, arbitrary_data)
P.show()