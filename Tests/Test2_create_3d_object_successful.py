from solid2 import *


d = cube(5) + sphere(5).right(5) - cylinder(r=2, h=6)

d.save_as_scad()
