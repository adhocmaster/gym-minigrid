exec(open("scripts/sys_path_hack.py").read())

from pedgrid.lib.BaseObject import BaseObject

import matplotlib.pyplot as plt

from pedgrid.perception.BasePerception import BasePerception
from pedgrid.perception.FOVPerception import FOVPerception
import random
from shapely.geometry import Polygon, MultiPolygon

from shapely.geometry import LineString


# Create some BaseObject instances
object1 = BaseObject((4, 5), (5, 4), "obstacle")
object2 = BaseObject((6, 7), (7, 6), "agent")
# Create the FOVPerception instance
fov_perception = FOVPerception()

# Define other necessary variables
agent_location = (1, 1)
grid_size = (10, 10)
objects = [object1, object2]  # List of BaseObject instances



# Call the getOG method
result = fov_perception.getOG(agent_location, grid_size, objects)

# The result will be a List of List[float], representing the occupation grid.
# You can further process or visualize the result as needed.
