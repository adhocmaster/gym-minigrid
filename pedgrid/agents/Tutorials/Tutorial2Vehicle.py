from pedgrid.agents.Vehicle import Vehicle
from pedgrid.lib.Action import Action
from pedgrid.lib.VehicleAction import VehicleAction

class Tutorial2Vehicle(Vehicle):
    
    def parallel1(self, env):
        return Action(self, VehicleAction.FORWARD)
    
    def parallel2(self, env):
        return None