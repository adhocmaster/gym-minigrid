#new method
#super is TaskEnv
#kind of like with multiLaneRoadEnv
#have all the lanes and stuff (look at ^) and methods
#register it at the end

from .TaskEnv import TaskEnv

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
from gym_minigrid.lib.SingleActions import SingleActions
from .EnvEvent import EnvEvent
import logging
import random

class EnvGrid(TaskEnv):
     def __init__(
        self,
        pedAgents: List[PedAgent]=[],
        vehicleAgents: List[Vehicle]=[],
        road: Road=None,
        sidewalks: List[Sidewalk]=[],
        crosswalks: List[Crosswalk]=[],
        gridWidth=8,
        gridHeight=8,
        stepsIgnore = 100
    ):
        
        self.vehicleAgents = vehicleAgents
        self.road = road
        self.sidewalks = sidewalks
        self.crosswalks = crosswalks
        
        super().__init__(
            pedAgents=pedAgents,
            width=gridWidth,
            height=gridHeight,
            stepsIgnore=stepsIgnore
        )
    
        self.updateActionHandlers({
            SingleActions: self.executePositionAction
            })
        # TODO label each tile with either lane/sidewalk?

        pass
     

    