import logging
from typing import Tuple, List

import numpy as np
import math

from pedgrid.agents import LaneNum
from pedgrid.lib.ObjectAction import ObjectAction

from .PedAgent import PedAgent
from pedgrid.lib.LaneAction import LaneAction
from pedgrid.lib.Action import Action
from pedgrid.lib.Direction import Direction

class ControllablePedAgent(PedAgent):
    """
    A simple pedestrian that moves forward
    """
    def __init__(self, id, position, direction, maxSpeed, speed):
        super().__init__(id, position, direction, maxSpeed, speed)
        self.nextParallel1 = None
        self.nextParallel2 = None

    def setNextParallel1(self, action: Action):
        self.nextParallel1 = action

    def setNextParallel2(self, action: Action):
        self.nextParallel2 = action
    
    def parallel1(self, env):
        """
            Simply move forward
        """
        action = self.nextParallel1
        self.nextParallel1 = None
        return action
    
    def parallel2(self, env):
        action = self.nextParallel2
        self.nextParallel2 = None
        return action