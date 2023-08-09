from .MultiLaneRoadEnv import MultiLaneRoadEnv

from typing import List
from gym_minigrid.minigrid import *
from gym_minigrid.register import register
from gym_minigrid.agents import *
from gym_minigrid.envs.pedestrian.PedGrid import PedGrid
from gym_minigrid.lib.Action import Action
from gym_minigrid.lib.LaneAction import LaneAction
from gym_minigrid.lib.ForwardAction import ForwardAction
from gym_minigrid.lib.Direction import Direction
from gym_minigrid.lib.VehicleAction import VehicleAction
from .EnvEvent import EnvEvent
import logging
import random

class TaskEnv(MultiLaneRoadEnv):
    # Write the outline here how it should work

    # generic object representation
    # generic actors?
    def __init__(
        self,
        pedAgents: List[PedAgent]=[],
        vehicleAgents: List[Vehicle]=[],
        road: Road=None,
        sidewalks: List[Sidewalk]=[],
        crosswalks: List[Crosswalk]=[],
        width=8,
        height=8,
        stepsIgnore = 100
    ):
        
        self.vehicleAgents = vehicleAgents
        self.road = road
        self.sidewalks = sidewalks
        self.crosswalks = crosswalks
        
        super().__init__(
            pedAgents=pedAgents,
            width=width,
            height=height,
            stepsIgnore=stepsIgnore
        )

        self.updateActionHandlers({VehicleAction : self.executeVehicleAction})
        # TODO label each tile with either lane/sidewalk?

        pass

class EnvGrid(TaskEnv):
    def __init__(self):
        width = 100 
        height = 100

        lane1 = Lane(
            topLeft=(10, 0),
            bottomRight=(24, 79),
            direction=1,
            inRoad=1,
            laneID=1,
            posRelativeToCenter=-1
        )
        lane2 = Lane(
            topLeft=(35, 0),
            bottomRight=(49, 79),
            direction=3,
            inRoad=1,
            laneID=2,
            posRelativeToCenter=1
        )
        road1 = Road([lane1, lane2], roadID=1)

        sidewalk1 = Sidewalk(
            topLeft=(0, 0),
            bottomRight=(9, 79),
            sidewalkID=1
        )

        sidewalk2 = Sidewalk(
            topLeft=(25, 0),
            bottomRight=(34, 79),
            sidewalkID=2
        )

        sidewalk3 = Sidewalk(
            topLeft=(50, 0),
            bottomRight=(59, 79),
            sidewalkID=3
        )

        crosswalk1 = Crosswalk(
            topLeft=(10, 40),
            bottomRight=(24, 45),
            crosswalkID=1,
            overlapRoad=1,
            overlapLanes=[1]
        )

        crosswalk2 = Crosswalk(
            topLeft=(35, 40),
            bottomRight=(49, 45),
            crosswalkID=2,
            overlapRoad=1,
            overlapLanes=[2]
        )

        super().__init__(
            road=road1,
            sidewalks=[sidewalk1, sidewalk2, sidewalk3],
            crosswalks=[crosswalk1, crosswalk2],
            width=width,
            height=height
        )

register(
    id='EnvGrid100x100-v0',
    entry_point='gym_minigrid.envs.pedestrian.TaskEnv:EnvGrid'
)