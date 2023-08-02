
from gym_minigrid.lib.Action import Action
from gym_minigrid.lib.ForwardAction import ForwardAction
from .PedAgent import PedAgent
from gym_minigrid.lib.LaneAction import LaneAction
import random

class TutorialPedAgent(PedAgent):

    """ Define a pedestrian that just moves forward in our Second env
    Assignment: make the pedestrian not always keep the same line."""
    
    def parallel1(self, env) -> Action:
        #raise NotImplementedError("parallel1 is not implemented")
        counter = random.randint(1, 4)
        if counter == 1:
            return Action(self, LaneAction.LEFT)
        elif counter == 2:
            return Action(self, LaneAction.RIGHT)
        else:
            return Action(self, ForwardAction.KEEP)


    def parallel2(self, env) -> Action:
        # raise NotImplementedError("parallel2 is not implemented")
        return None