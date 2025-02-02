from pedgrid.agents.Vehicle import Vehicle
from pedgrid.lib.Action import Action
from pedgrid.lib.VehicleAction import VehicleAction

class SimpleVehicle(Vehicle):
    """
    A simple vehicle that moves forward
    """
    def __init__(self, id, topLeft, bottomRight, direction, maxSpeed, speed, inRoad, inLane):
        super().__init__(id, topLeft, bottomRight, direction, maxSpeed, speed, inRoad, inLane)
    
    def parallel1(self, env):
        """
            Simply move forward
        """
        return Action(self, VehicleAction.FORWARD)
    
    def parallel2(self, env):
        """
            Simply move forward
        """
        return None