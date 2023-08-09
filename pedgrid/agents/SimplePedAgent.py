

from pedgrid.lib.ObjectAction import ObjectAction

from .PedAgent import PedAgent
from pedgrid.lib.Action import Action

class SimplePedAgent(PedAgent):
    """
    A simple pedestrian that moves forward
    """
    def __init__(self, id, position, direction, maxSpeed, speed):
        super().__init__(id, position, direction, maxSpeed, speed)
    
    def parallel1(self, env):
        """
            Simply move forward
        """
        return Action(self, ObjectAction.FORWARD)
    
    def parallel2(self, env):
        pass