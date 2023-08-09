from pedgrid.lib.Action import Action
from pedgrid.lib.ObjectAction import ObjectAction
from pedgrid.lib.LaneAction import LaneAction
from pedgrid.agents.PedAgent import PedAgent
import numpy as np

class Tutorial1PedAgent(PedAgent):
    
    def parallel1(self, env) -> Action:
        return Action(self, ObjectAction.FORWARD)
        # return None

    def parallel2(self, env) -> Action:
        return np.random.choice([Action(self, LaneAction.LEFT), Action(self, LaneAction.RIGHT)], p=(0.5, 0.5))
        # return None