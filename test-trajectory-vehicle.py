import gym
import pedgrid


from pedgrid.agents.TrajectoryVehicle import TrajectoryVehicle
from pedgrid.lib.Direction import Direction
import time

env = gym.make("EnvGrid100x100-v0")
env.reset()

vehicle1 = TrajectoryVehicle(
    id=1,
    trajectory = [12, 12, 14, 14, 16, 16, 18, 18, 20, 20]
    topLeft=(10, 10),
    bottomRight=(15, 20),
    direction=2,
    maxSpeed=1.0,
    speed=0.5,
    inRoad=1,
    inLane=1,
)

env.addTrajectoryVehicleAgent(vehicle1)


#Move the vehicle along the trajectory
for i in range(5):
    env.step(None)
    env.render()
    time.sleep(2)
env.close()