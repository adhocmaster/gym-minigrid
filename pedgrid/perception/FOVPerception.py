#exec(open("scripts/sys_path_hack.py").read())

import pdb

import sys
import numpy as np
import math
from typing import List, Tuple


from pedgrid.lib.BaseObject import BaseObject
from pedgrid.perception.BasePerception import BasePerception

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


class FOVPerception(BasePerception):
    def getOG(self, agentLocation: Tuple[int, int], gridSize: Tuple[int, int], objects: List[BaseObject]) -> List[List[float]]:

        Car = []
        print(objects[0].topLeft[0])
        for i in range(len(objects)):
            shapely_polygon1 = Polygon([(objects[i].topLeft[0], objects[i].topLeft[1]),
                                (objects[i].bottomRight[0], objects[i].topLeft[1]),
                                (objects[i].bottomRight[0], objects[i].bottomRight[1]),
                                (objects[i].topLeft[0], objects[i].bottomRight[1])])
            print(shapely_polygon1.is_valid)
            Car.append(shapely_polygon1)

        print(Car[0].is_valid)
        Car = MultiPolygon(Car)
        print(Car.geoms[0].is_valid)

        

        occupation_grid= []

        def createGrid() -> 'list':
            grid = []
            for i in range(gridSize[0]):
                for j in range(gridSize[1]):
                    Grid = box(10*i, 10*j, 10*i+10, 10*j+10)
                    grid.append(Grid)
                    x1, y1 = Grid.exterior.xy
                    plt.plot(x1, y1, color="black", linewidth=0.5)
            return grid

        grid = createGrid()

        for i in range(len(grid)):
            occupation_grid.append(0.0)

        #this is the main part of the function here we iterate through each object draw appropriate lines and create a polygon representing the blind spot
        for i in range(len(Car.geoms)):

            exterior_ring1 = Car.geoms[i]
            print(exterior_ring1)
            vertices_coords1 = list(exterior_ring1.coords)  
            print(vertices_coords1)

            def remove_closest_furthest(vertices_coords1: List[Tuple[float, float]], agent_location: Tuple[float, float]) -> Tuple[Tuple[float, float], Tuple[float, float]]:

                def distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
                    x1, y1 = point1
                    x2, y2 = point2
                    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

                # Get the closest and furthest points from the pedestrian
                distances = [distance(vertex, agent_location) for vertex in vertices_coords1] # stores each distance from vertice coords
                closest_point_index = np.argmin(distances)
                furthest_point_index = np.argmax(distances)

                # Remove the closest and furthest points from vertices_coords1 save the furthest to be used later
                vertices_coords1.pop(closest_point_index)
                furthest_point = vertices_coords1.pop(furthest_point_index - 1 if furthest_point_index > closest_point_index else furthest_point_index)

                return furthest_point

            vertice_max = remove_closest_furthest(vertices_coords1, agentLocation)

            def extend_line(agentLocation, vertices_coords, vertex_index, extension_length=100):

                vertex_coords = vertices_coords[vertex_index]
                dx = vertex_coords[0] - agentLocation[0]
                dy = vertex_coords[1] - agentLocation[1]
                magnitude = (dx ** 2 + dy ** 2) ** 0.5
                unit_vector_x = dx / magnitude
                unit_vector_y = dy / magnitude
                new_endpoint_x = vertex_coords[0] + unit_vector_x * extension_length
                new_endpoint_y = vertex_coords[1] + unit_vector_y * extension_length

                extended_line = LineString([(agentLocation[0], agentLocation[1]), (new_endpoint_x, new_endpoint_y)])
                return extended_line

            extended_line0 = extend_line(agentLocation, vertices_coords1, 0, len(grid))
            extended_line1 = extend_line(agentLocation, vertices_coords1, 1, len(grid))


            s2, t2 = extended_line0.xy
            plt.plot(s2, t2, color="green")
            s3, t3 = extended_line1.xy
            plt.plot(s3, t3, color="green")


            def NotVisiblePolygon():
                grid_boundary = box(0, 0, 100, 100)
                x, y = grid_boundary.exterior.xy
                plt.plot(x, y, color="blue", alpha=0.5)
                intersection1 = grid_boundary.intersection(extended_line0)
                intersection2 = grid_boundary.intersection(extended_line1)

                intersection11 = intersection1.coords[1]
                intersection22 = intersection2.coords[1]

                # Create the polygon representing the field of view behind the car
                rear_polygon_coords = [vertices_coords1[0]]

                #rear_polygon_coords.append(vertices_coords1[0])
                rear_polygon_coords.append(vertice_max)
                rear_polygon_coords.append(vertices_coords1[1])
                rear_polygon_coords.append(intersection22)
                if ((intersection1.coords[1][0] == 0.0 and intersection1.coords[1][1] != 100.0 and intersection2.coords[1][0] != 0.0 and intersection2.coords[1][1] == 100.0) or (intersection1.coords[1][0] != 0.0 and intersection2.coords[1][0] == 0.0 and intersection2.coords[1][1] != 100.0 and intersection1.coords[1][1] == 100.0)):
                    rear_polygon_coords.append((0.0, 100.0))
                elif ((intersection1.coords[1][0] == 100.0 and intersection2.coords[1][0] != 100.0 and intersection2.coords[1][1] == 100.0) or (intersection1.coords[1][0] != 100.0 and intersection2.coords[1][0] == 100.0 and intersection1.coords[1][1] == 100.0)):
                    rear_polygon_coords.append((100.0, 100.0))
                elif ((intersection1.coords[1][0] == 0.0 and intersection2.coords[1][0] != 0.0 and intersection2.coords[1][0] != 0.0) or (intersection1.coords[1][0] != 0.0 and intersection2.coords[1][0] == 0.0 and intersection2.coords[1][1] != 0.0)):
                    rear_polygon_coords.append((0.0, 0.0))
                elif ((intersection1.coords[1][0] == 100.0 and intersection2.coords[1][0] != 100.0 and intersection2.coords[1][1] == 0.0) or (intersection1.coords[1][0] != 100.0 and intersection2.coords[1][0] == 100.0 and intersection1.coords[1][1] == 0.0)):
                    rear_polygon_coords.append((100.0, 0.0))
                rear_polygon_coords.append(intersection11)


                rear_polygon = Polygon(rear_polygon_coords)

                x, y = rear_polygon.exterior.xy
                plt.plot(x, y, color="black", alpha=0.5)
                plt.fill(x ,y, alpha=1, color="blue")

                return rear_polygon

            def fillNotVisiblePolygon():
                for i in range(len(grid)):
                    if ((grid[i]).intersects(NotVisiblePolygon())):
                        occupation_grid[i] = (0.5)
            fillNotVisiblePolygon()

        def fillOccupancyGrid():
            for i in range(len(grid)):
                if ((occupation_grid[i]) == 0.5):
                    occupation_grid[i] = (0.5)
                elif (grid[i]).intersects(Car):
                    occupation_grid[i] = (1.0)
                else:
                    occupation_grid[i] = (0.0)
 
        fillOccupancyGrid()

        # Convert the list to a 10x10 2D list
        cols = int(math.sqrt(len(grid)))
        occupation_grid = [occupation_grid[i:i + cols] for i in range(0, len(occupation_grid), cols)]

        # Print the result
        for row in occupation_grid:
            print(row)

        plt.title("line")
        plt.show()

        return occupation_grid
