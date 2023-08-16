
from calendar import c
import random
import gym
import pedgrid
from typing import Tuple
from pedgrid.agents.Agent import Agent
from pedgrid.agents.Vehicle import Vehicle
from pedgrid.lib.Action import Action
from pedgrid.lib.PositionAction import PositionAction
from pedgrid.rendering import fill_coords, point_in_line, point_in_rect


class RandomTrajectoryVehicle(Vehicle):
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

    def parallel1(self, env) -> Action:
          return Action(self, PositionAction.KEEP)
    
    def parallel2(self, env) -> Action:
          return None

    def generateTrajectory(self, start, end , step_count):
        trajectory = [start]
        for i in range(step_count - 1):
            x = random.uniform(0.0, 1.0)
            y = random.uniform(0.0, 1.0)
            waypoint = (start[0] + x * (end[0] - start[0]), start[1] + y * (end[1] - start[1]))
            trajectory.append(waypoint)
        trajectory.append(end)
        return trajectory