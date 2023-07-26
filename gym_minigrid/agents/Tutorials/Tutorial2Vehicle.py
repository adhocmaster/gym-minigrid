from gym_minigrid.agents.Vehicle import Vehicle
from gym_minigrid.lib.Action import Action
from gym_minigrid.lib.VehicleAction import VehicleAction

class Tutorial2Vehicle(Vehicle):
    
    def parallel1(self, env):
        return Action(self, VehicleAction.KEEP)