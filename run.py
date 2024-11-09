#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
starts application and plots features defined in plot.xml
"""

import tkinter as tk
import numpy as np
import xml.etree.ElementTree as et

# setup window
window = tk.Tk()
window.title('Land Manager')

# create a canvas widget
canvas = tk.Canvas(window, width=10000, height=10000)
canvas.pack()

# retrieve plot data from plot.xml
xml = et.parse('plot.xml')
plot = xml.getroot()

# retrieve the vertices of the property
boundary = plot.find('property').find('polygon')
vertices = []
for v in boundary.findall('vertex'):
    vertices.append(float(v.find('x-coord').text))
    vertices.append(float(v.find('y-coord').text))
points = np.array(vertices)

# draw the property polygon
points = points * 100000
points = points + 500
canvas.create_polygon(points.tolist(), fill='lightblue', outline='blue', width=2)

window.mainloop()
