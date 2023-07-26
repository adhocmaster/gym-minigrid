import time
import gym
import gym_minigrid
from gym_minigrid.agents import *
import logging
env = gym.make('TwoLaneRoadEnv30x80-v0')       
env.reset()

v1 = SimpleVehicle(1, (7, 10), (12, 19), 1, 5, 5, 1, 1)
v2 = SimpleVehicle(2, (17, 60), (22, 69), 3, 5, 5, 1, 2)
p1 = Tutorial2PedAgent(ids=1, position=(0, 42), direction=Direction.East, maxSpeed=3, speed = 3)
p2 = Tutorial2PedAgent(id=2, position=(29,44), direction=Direction.West, maxSpeed=3, speed = 3)
p3 = Tutorial2PedAgent(id=3, position=(2,5), direction=Direction.South, maxSpeed=3, speed = 3)
p4 = Tutorial2PedAgent(id=4, position=(27,74), direction=Direction.North, maxSpeed=3, speed = 3)

env.addVehicleAgent(v1)
env.addVehicleAgent(v2)
env.addPedAgent(p1)
env.addPedAgent(p2)
env.addPedAgent(p3)
env.addPedAgent(p4)

for i in range(110):

    obs, reward, done, info = env.step(None)
    
    if done:
        "Reached the goal"
        break

    env.render()

    if i % 10 == 0:
        logging.info(f"Completed step {i+1}")

    time.sleep(0.5)