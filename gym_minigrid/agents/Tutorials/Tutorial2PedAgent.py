from gym_minigrid.lib.Action import Action
from gym_minigrid.lib.ForwardAction import ForwardAction
from gym_minigrid.lib.LaneAction import LaneAction
from gym_minigrid.agents.PedAgent import PedAgent
import numpy as np

class Tutorial2PedAgent(PedAgent):
    
    def parallel1(self, env) -> Action:
        return Action(self, ForwardAction.KEEP)
        # return None

    def parallel2(self, env) -> Action:
        return None