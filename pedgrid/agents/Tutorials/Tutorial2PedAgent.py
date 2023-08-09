from pedgrid.lib.Action import Action
from pedgrid.lib.ObjectAction import ObjectAction
from pedgrid.lib.LaneAction import LaneAction
from pedgrid.agents.PedAgent import PedAgent
import numpy as np

class Tutorial2PedAgent(PedAgent):
    
    def parallel1(self, env) -> Action:
        return Action(self, ObjectAction.FORWARD)
        # return None

    def parallel2(self, env) -> Action:
        return None