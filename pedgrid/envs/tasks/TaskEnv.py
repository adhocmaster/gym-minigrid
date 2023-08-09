from pedgrid.agents.Agent import Agent
from pedgrid.objects import *
from pedgrid.envs.pedestrian.PedestrianEnv import PedestrianEnv

from typing import List, Tuple
from ..pedestrian.EnvEvent import EnvEvent
import logging
import random

from dataclasses import dataclass, field

@dataclass
class TaskEnv:
    env: PedestrianEnv = None
    agents: List[Agent] = field(default_factory=list)
    objects: List[BaseObject] = field(default_factory=list)


