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

        obsticlePolygons = self._objsToMultiPolygon(objects)

        grid = self._createGrid(gridSize)

        occupation_grid = self._fillOccupationGridtoZero(grid)

        #this is the main part of the function here we iterate through each object draw appropriate lines and create a polygon representing the blind spot
        for i in range(len(obsticlePolygons.geoms)):

            exterior_ring1 = obsticlePolygons.geoms[i]
            print(exterior_ring1)
            vertices_coords = list(exterior_ring1.exterior.coords)  

            vertice_max = self._get_closest_furthest(vertices_coords, agentLocation)[0]

            vertices_coords = self._remove_closest_furthest(vertices_coords, agentLocation) #this is the vertices_coords with the furthest and closest points removed and I will not need the older version

             
            LineagentToVertexAndBeyondGrid0 = self._extend_line(agentLocation, vertices_coords, 0, gridSize)
            LineagentToVertexAndBeyondGrid1 = self._extend_line(agentLocation, vertices_coords, 1, gridSize)


            self._plotLine(self._getLineCoords(LineagentToVertexAndBeyondGrid0)[0], self._getLineCoords(LineagentToVertexAndBeyondGrid0)[1])
            self._plotLine(self._getLineCoords(LineagentToVertexAndBeyondGrid1)[0], self._getLineCoords(LineagentToVertexAndBeyondGrid1)[1])

    
            self._fillNotVisiblePolygon(grid, occupation_grid, vertices_coords, LineagentToVertexAndBeyondGrid0, LineagentToVertexAndBeyondGrid1, vertice_max, gridSize)
 
        self._fillOccupancyGrid(grid, occupation_grid, obsticlePolygons)

        occupation_grid = self._1dTo2dGrid(occupation_grid, gridSize[0], gridSize[1])
        
        self._printOccupationGrid(occupation_grid)

        return occupation_grid
    
    

    def _createGrid(self, gridSize: Tuple[int, int]) -> 'list':
        grid = []
        for i in range(gridSize[0]):
            for j in range(gridSize[1]):
                cell = box((gridSize[0]/10)*i, (gridSize[1]/10)*j, (gridSize[0]/10)*i+1, (gridSize[1]/10)*j+1)
                grid.append(cell)
        return grid

    
    def _plotPoly(self, poly: Polygon, color="black", linewidth=0.5):
        x1, y1 = poly.exterior.xy
        plt.plot(x1, y1, color=color, linewidth=linewidth)
        plt.show()

    def _fillOccupationGridtoZero(self, grid: List) -> List:
        Zero = []
        for i in range(len(grid)):
            Zero.append(0.0)
        return Zero

    def _objToPolygon(self, obj: BaseObject) -> Polygon:
        polygon = Polygon([
                (obj.topLeft[0], obj.topLeft[1]),
                (obj.bottomRight[0], obj.topLeft[1]),
                (obj.bottomRight[0], obj.bottomRight[1]),
                (obj.topLeft[0], obj.bottomRight[1]),
                (obj.topLeft[0], obj.topLeft[1])  # Close the ring by repeating the first point.
                        ])
        assert polygon.is_valid
        return polygon
    
    def _objsToMultiPolygon(self, objs: List[BaseObject]) -> MultiPolygon:
        polygons = []
        for obj in objs:
            polygons.append(self._objToPolygon(obj))
        
        return MultiPolygon(polygons)
    
    def _distance(self, point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        x1, y1 = point1
        x2, y2 = point2
        return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    def _get_closest_furthest(self, vertices_coords: List[Tuple[float, float]], agent_location: Tuple[float, float]) -> Tuple[Tuple[float, float], Tuple[float, float]]:

        # Get the closest and furthest points from the pedestrian
        distances = [self._distance(vertex, agent_location) for vertex in vertices_coords] # stores each distance from vertice coords
        closest_point_index = np.argmin(distances)
        furthest_point_index = np.argmax(distances)

        return vertices_coords[furthest_point_index], vertices_coords[closest_point_index]

    
    def _remove_closest_furthest(self, vertices_coords: List[Tuple[float, float]], agent_location: Tuple[float, float] ) -> Tuple[Tuple[float, float], Tuple[float, float]]:

        vertices_coords_temp = vertices_coords
        furthest_point, closest_point = self._get_closest_furthest(vertices_coords, agent_location)

        # Remove the closest and furthest points from vertices_coords save the furthest to be used later
        closest_point = vertices_coords_temp.remove(closest_point)
        furthest_point = vertices_coords_temp.remove(furthest_point)

        return vertices_coords_temp
    
    def _extend_line(self, agentLocation: Tuple[int, int], vertices_coords: List[Tuple[float, float]], vertex_index: int, gridSize: Tuple[int, int]) -> LineString:

        extension_length = (1.5*gridSize[0])
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
    
    def _getLineCoords(self, line: LineString) -> Tuple[List[float], List[float]]:
        x, y = line.xy
        return x, y
    
    def _plotLine(self, x: List[float], y: List[float]):
        plt.plot(x, y, color="green")

    def _fillNotVisiblePolygon(self, grid, occupation_grid, vertices_coords: List[Tuple[float, float]], LineagentToVertexAndBeyondGrid0, LineagentToVertexAndBeyondGrid1, vertice_max, gridSize):
        for i in range(len(grid)):
            if ((grid[i]).intersects(self._NotVisiblePolygon(vertices_coords, LineagentToVertexAndBeyondGrid0, LineagentToVertexAndBeyondGrid1, vertice_max, gridSize))):
                occupation_grid[i] = (0.5)

    #needs to be fixed so that it can adjust itself to other sizes of grid
    def _NotVisiblePolygon(self, vertices_coords: List[Tuple[float, float]], LineagentToVertexAndBeyondGrid0, LineagentToVertexAndBeyondGrid1, vertice_max, gridSize):
        grid_boundary = box(0, 0, gridSize[0], gridSize[1])
        x, y = grid_boundary.exterior.xy
        plt.plot(x, y, color="blue", alpha=0.5)
        intersection1 = grid_boundary.intersection(LineagentToVertexAndBeyondGrid0)
        intersection2 = grid_boundary.intersection(LineagentToVertexAndBeyondGrid1)

        intersection11 = intersection1.coords[1]
        intersection22 = intersection2.coords[1]

        # Create the polygon representing the field of view behind the obsticlePolygons
        rear_polygon_coords = [vertices_coords[0]]

        #rear_polygon_coords.append(vertices_coords[0])
        rear_polygon_coords.append(vertice_max)
        rear_polygon_coords.append(vertices_coords[1])
        rear_polygon_coords.append(intersection22)
        if ((intersection1.coords[1][0] == 0.0 and
             intersection1.coords[1][1] != gridSize[1] and
             intersection2.coords[1][0] != 0.0 and
             intersection2.coords[1][1] == gridSize[1]) or
             (intersection1.coords[1][0] != 0.0 and
             intersection2.coords[1][0] == 0.0 and
             intersection2.coords[1][1] != gridSize[1] and
             intersection1.coords[1][1] == gridSize[1])):
            rear_polygon_coords.append((0.0, gridSize[1]))
        elif ((intersection1.coords[1][0] == gridSize[0] and
             intersection2.coords[1][0] != gridSize[0] and
             intersection2.coords[1][1] == gridSize[1]) or
             (intersection1.coords[1][0] != gridSize[0] and
             intersection2.coords[1][0] == gridSize[0] and
             intersection1.coords[1][1] == gridSize[1])):
            rear_polygon_coords.append((gridSize[0], gridSize[1]))
        elif ((intersection1.coords[1][0] == 0.0 and
             intersection2.coords[1][0] != 0.0 and
             intersection2.coords[1][0] != 0.0) or
             (intersection1.coords[1][0] != 0.0 and
             intersection2.coords[1][0] == 0.0 and
             intersection2.coords[1][1] != 0.0)):
            rear_polygon_coords.append((0.0, 0.0))
        elif ((intersection1.coords[1][0] == gridSize[0] and
             intersection2.coords[1][0] != gridSize[0] and
             intersection2.coords[1][1] == 0.0) or
             (intersection1.coords[1][0] != gridSize[0] and
             intersection2.coords[1][0] == gridSize[0] and
             intersection1.coords[1][1] == 0.0)):
            rear_polygon_coords.append((gridSize[0], 0.0))

        rear_polygon_coords.append(intersection11)
        rear_polygon = Polygon(rear_polygon_coords)

        x, y = rear_polygon.exterior.xy
        plt.plot(x, y, color="black", alpha=0.5)
        plt.fill(x ,y, alpha=1, color="blue")

        return rear_polygon
    
    def _fillOccupancyGrid(self, grid: list, occupation_grid: List[float], obsticlePolygons):
        for i in range(len(grid)):
            if ((occupation_grid[i]) == 0.5):
                occupation_grid[i] = (0.5)
            elif (grid[i]).intersects(obsticlePolygons):
                occupation_grid[i] = (1.0)
            else:
                occupation_grid[i] = (0.0)
        
    def _1dTo2dGrid(self, occupation_grid: List[float], rows: int, columns: int):
        if rows * columns != len(occupation_grid):
            return None  # Invalid input, the list size doesn't match the grid size
    
        twoDimensionalOccupationGrid = []
        for i in range(rows):
            row = occupation_grid[i * columns: (i + 1) * columns]
            twoDimensionalOccupationGrid.append(row)
    
        return twoDimensionalOccupationGrid
    
    def _printOccupationGrid(self, occupation_grid: List[float]):
        for row in occupation_grid:
            print(row)

        plt.title("line")
        plt.show()

