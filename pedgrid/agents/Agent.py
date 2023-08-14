from typing import Tuple
from pedgrid.objects.BaseObject import BaseObject
import random
import numpy as np
from pedgrid.lib.Action import Action
from abc import abstractmethod

class Agent(BaseObject):
    def __init__(
        self, 
        id,
        topLeft: Tuple[int, int],
        bottomRight: Tuple[int, int],
        direction: int, # TODO convert direction to enum
        maxSpeed: float = 4,
        speed: float = 3,
        objectType="Agent"
    ):

        self.id = id

        super().__init__(
            topLeft=topLeft,
            bottomRight=bottomRight,
            objectType=objectType
        )

        self.initTopLeft = topLeft
        self.initBottomRight = bottomRight
        self.initDirection = direction

        self.direction = direction
        self.maxSpeed = maxSpeed
        self.speed = speed

        self.canShiftLeft = True
        self.canShiftRight = True
        self.agentAction = 0 # Put this in PedAgent later, save agentActions here for execution
        # Agents will save the actions we compute
        # Once we execute, we get action from here
        
        self.gapSame = 8 # TODO transfer all the blue and alder properties
        self.gapOpp = 4
        
        pass

    def reset(self):
        # TODO 
        self.topLeft = self.initTopLeft
        self.bottomRight = self.initBottomRight
        self.direction = self.initDirection
        pass

    def positionMove(self, stepCount):
            print ("moving position")
            assert self.direction >= 0 and self.direction < 4
            #Terry - uses the direction to left of agent to find vector to move left
            # left_dir = agent.direction - 1
            # if left_dir < 0:
            #     left_dir += 4
            # left_pos = agent.position + DIR_TO_VEC[left_dir]

            # agent.position[0] = left_pos
            step_count=stepCount
            nextPoint=self.trajectory[step_count]
            newTopLeftx = nextPoint[0]
            newBottomRightx = self.bottomRight[0]+(nextPoint[0]-self.topLeft[0])
            newTopLefty = nextPoint[1]
            newBottomRighty = self.bottomRight[1]+(nextPoint[1]-self.topLeft[1])
            self.topLeft = (newTopLeftx, newTopLefty)
            self.bottomRight = (newBottomRightx, newBottomRighty)


    @abstractmethod
    def parallel1(self, env) -> Action:
        raise NotImplementedError("parallel1 is not implemented")

    @abstractmethod
    def parallel2(self, env) -> Action:
        raise NotImplementedError("parallel2 is not implemented")

    