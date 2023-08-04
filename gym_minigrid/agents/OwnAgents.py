import gym
import gym_minigrid
from typing import Tuple
from gym_minigrid.agents.Agent import Agent
from gym_minigrid.agents.Vehicle import Vehicle
from gym_minigrid.lib.Action import Action
from gym_minigrid.lib.SingleActions import SingleActions


class TrajectoryVehicle(Vehicle):
    def __init__(
        self,
        id,
        topLeft: Tuple[int, int],
        bottomRight: Tuple[int, int],
        direction: int,
        maxSpeed: float,
        speed: float,
        inRoad: int,
        inLane: int,
        trajectory=[(12, 12), (14, 14), (16, 16), (20, 20), (22, 22)], #fixed trajectory
        objectType="Vehicle"
        ):
            super().__init__(
                inRoad=int,
                inLane=int,
                id=id,
                topLeft=topLeft,
                bottomRight=bottomRight,
                direction=direction,
                maxSpeed=maxSpeed,
                speed=speed,
                objectType=objectType
            )
        
            self.inRoad = inRoad
            self.inLane = inLane
            self.trajectory = trajectory
            
    def parallel1(self, env) -> Action:
          return Action(self, SingleActions.POSITION)
    
    def parallel2(self, env) -> Action:
          return None
