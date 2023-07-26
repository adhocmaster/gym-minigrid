import time
import logging
import gym
import gym_minigrid
from gym_minigrid.agents import *

env = gym.make('PedestrianEnv-20x80-v0')
env.reset()

ped = Tutorial1PedAgent(id=1, position=(10, 10), direction=Direction.East, maxSpeed=3, speed=3)
env.addPedAgent(ped)

for i in range(100):

    obs, reward, done, info = env.step(None)
    
    if done:
        "Reached the goal"
        break

    env.render()

    if i % 10 == 0:
        logging.info(f"Completed step {i+1}")

    time.sleep(0.5)