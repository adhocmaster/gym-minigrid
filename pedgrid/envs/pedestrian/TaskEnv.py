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