from gym_minigrid import register
from gym_minigrid.agents.Agent import Agent
from .MultiPedestrianEnv import MultiPedestrianEnv


class CrosswalkEnv(MultiPedestrianEnv):


    
    def __init__(
        self,
        agents: list[Agent]=None,
        width=8,
        height=8,
        crosswalkPosition=None,
        crosswalkOrigin=None,
        crosswalkSize = 3
    ):

        super().__init__(agents, width, height)

        if crosswalkPosition is None:
            crosswalkPosition = (0, (height // 2) - (crosswalkSize // 2))
        
        if crosswalkOrigin is None:
            crosswalkOrigin = (width // 2, crosswalkPosition[1] + (crosswalkSize // 2))

        self.crosswalkOrigin = crosswalkOrigin
        self.crosswalkPosition = crosswalkPosition
        self.crosswalkSize = crosswalkSize

    
    def getCrossWalkPoint(self, worldPoint):
        return (worldPoint[0] - self.crosswalkOrigin[0], worldPoint[1] - self.crosswalkOrigin[1])

register(
    id='Crosswalk-Empty-20x80-v0',
    entry_point='gym_minigrid.envs.pedestrian.CrosswalkEnv:CrosswalkEnv',
)
