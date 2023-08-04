import gym
import gym_minigrid
from typing import Tuple
from gym_minigrid.agents.Agent import Agent
from gym_minigrid.agents.Vehicle import Vehicle
from gym_minigrid.lib.Action import Action
from gym_minigrid.lib.PositionAction import PositionAction
from gym_minigrid.rendering import fill_coords, point_in_line, point_in_rect



class TrajectoryVehicle(Vehicle):
    def __init__(
        self,
        id,
        trajectory: list,
        topLeft: Tuple[int, int],
        bottomRight: Tuple[int, int],
        direction: int,
        maxSpeed: float,
        speed: float,
        inRoad: int,
        inLane: int,
        ):
            super().__init__(
                inRoad=int,
                inLane=int,
                id=id,
                topLeft=topLeft,
                bottomRight=bottomRight,
                direction=direction,
                maxSpeed=maxSpeed,
                speed=speed
            )
        
            self.inRoad = inRoad
            self.inLane = inLane
            self.trajectory = trajectory
            
    def parallel1(self, env) -> Action:
          return Action(self, PositionAction.KEEP)
    
    def parallel2(self, env) -> Action:
          return None
