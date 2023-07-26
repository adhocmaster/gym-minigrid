import time
import logging
import gym
import gym_minigrid
from gym_minigrid.agents import *

env = gym.make('PedestrianEnv-20x80-v0')
env.reset()

