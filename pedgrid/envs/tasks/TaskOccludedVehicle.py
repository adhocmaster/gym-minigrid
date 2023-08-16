import gym
from pedgrid.agents.ControllablePedAgent import ControllablePedAgent
from pedgrid.agents.PedAgent import PedAgent
from pedgrid.agents.SimplePedAgent import SimplePedAgent
from pedgrid.agents.TrajectoryVehicle import TrajectoryVehicle
from pedgrid.agents.Vehicle import Vehicle
from pedgrid.envs.pedestrian.MultiLaneRoadEnv import MultiLaneRoadEnv
from pedgrid.envs.pedestrian.PedestrianEnv import PedestrianEnv
from pedgrid.envs.tasks.TaskEnv import TaskEnv
from pedgrid.lib import LaneAction, ObjectAction
from pedgrid.lib.Direction import Direction
from pedgrid.objects import *
from typing import *
from pedgrid.register import register


class TaskOccludedVehicle(TaskEnv):

    def __init__(self):
        
        env = self.createEnv()

        # todo, create our vehicle and obsticle
        # todo, the pedestrian object will be created by the research itself.

        self.pedAgent = self.createPedestrian()
        vehicleAgent = self.createVehicle(env)
        objects = self.createObjects(env)

        agents = [self.pedAgent, vehicleAgent]

        super().__init__(
            env=env,
            agents=agents,
            objects=objects
        )
        pass

    def createPedestrian(self, env: MultiLaneRoadEnv) -> ControllablePedAgent:
        # set the position of the pedestrian to a predefined position
        # add it to the environment.
        ped = ControllablePedAgent(
            id=1,
            position=(50, 10),
            direction=Direction.RIGHT,
            maxSpeed=2,
            speed=1
        )
        env.addPedAgent(ped)
        return ped
    

    def createVehicle(self, env: MultiLaneRoadEnv) -> Vehicle: #maybe change to the new vehicle agent Rishi makes
        vehicle1 = TrajectoryVehicle(
            id=1,
            topLeft=(16, 20),
            bottomRight=(29, 60),
            trajectory=(), #fill in the trajectory points
            direction=2,
            maxSpeed=2,
            speed=1
        )
        env.addVehicleAgent(vehicle1)
        return vehicle1
    
    def createObjects(self, env: MultiLaneRoadEnv) -> List[BaseObject]: #is this needed still?
        baseObjects: List[BaseObject]
        obstacle = BaseObject(
            topLeft=(45, 20),
            bottomRight=(58, 65)
        )
        baseObjects.append(obstacle)
        return baseObjects
    

    def createEnv(self) -> MultiLaneRoadEnv:
        width = 60
        height = 200

        lane1 = Lane(
            topLeft=(15, 0),
            bottomRight=(30, 200),
            direction=1,
            inRoad=1,
            laneID=1,
            posRelativeToCenter=-1
        )
        lane2 = Lane(
            topLeft=(30, 0),
            bottomRight=(45, 200),
            direction=3,
            inRoad=1,
            laneID=2,
            posRelativeToCenter=1
        )

        road = Road([lane1, lane2], roadID=1)

        sidewalk1 = Sidewalk(
            topLeft=(0, 0),
            bottomRight=(15, 200),
            sidewalkID=1
        )

        sidewalk2 = Sidewalk(
            topLeft=(45, 0),
            bottomRight=(60, 200),
            sidewalkID=2
        )

        return MultiLaneRoadEnv(
            pedAgents=[],
            vehicleAgents=[],
            road=road,
            sidewalks=[sidewalk1, sidewalk2],
            #crosswalks=[crosswalk1],
            width=width,
            height=height,
            stepsIgnore=100
        )


    def step(self, action: int):

        # todo, modify 

        if action == 0:
            self.pedAgent.setNextParallel1(ObjectAction.FORWARD)

        if action == 1:
            self.pedAgent.setNextParallel1(LaneAction.LEFT)

        if action == 2:
            self.pedAgent.setNextParallel1(LaneAction.RIGHT)

        obs, reward, done, info = super().step()

        pass

    def getActions() -> dict:
        return {
            "Forward": 0,
            "Left": 1,
            "Right": 2,
            "None": 3
        }

        
register(
    id='TaskOccludedVehicle-v0',
    entry_point='gym_minigrid.envs.pedestrian.TaskOccludedVehicle:TaskOccludedVehicle'
)

