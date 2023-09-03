#exec(open("scripts/sys_path_hack.py").read())

import pdb

import sys
import numpy as np
import math
from typing import List, Tuple

import matplotlib.pyplot as plt

from shapely.ops import polygonize
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import MultiLineString
from shapely.geometry import CAP_STYLE, JOIN_STYLE
from shapely.ops import cascaded_union
from shapely.geometry import box
from shapely.geometry import LineString
from shapely.geometry import LinearRing
from shapely.geometry import Point 
import random


import numpy as np
from shapely.geometry import Polygon, Point



# Define the coordinates of the rectangle's corners
rectangle_coords = [(0, 0), (0, 4), (6, 4), (6, 0)]

# Create a Shapely Polygon object representing the rectangle
rectangle = Polygon(rectangle_coords)

# Access the underlying geometric representation using .geom
raw_geom = rectangle.geom

# Print the raw geometric representation
print(raw_geom)