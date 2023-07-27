import gym
import gym_minigrid

from gym_minigrid.agents import Vehicle
from gym_minigrid.agents.TrajectoryVehicle import TrajectoryVehicle
from gym_minigrid.agents.SimpleVehicle import SimpleVehicle
from gym_minigrid.lib.Direction import Direction
import time

env = gym.make("TwoLaneRoadEnv60x80-v0")
env.reset()

vehicle1 = TrajectoryVehicle(
    id=1,
    topLeft=(10, 10),
    bottomRight=(15, 20),
    trajectory=[10, 10, 12, 12, 14, 14, 16, 16, 20, 20, 22, 22], #coordinates of topLeft corner, without parathenses
    direction=2,
    maxSpeed=1.0,
    speed=0.5,
    inRoad=1,
    inLane=1,
)

#v2 = SimpleVehicle(1, (14, 20), (20, 29), 1, 5, 5, 1, 1)

env.addTrajectoryVehicleAgent(vehicle1)
#env.addVehicleAgent(v2)


#Move the vehicle along the trajectory
for i in range(5):
    env.step(None)
    env.render()
    time.sleep(2)
env.close()