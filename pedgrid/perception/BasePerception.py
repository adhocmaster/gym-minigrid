from typing import List, Tuple

from pedgrid.lib import BaseObject
from abc import abstractmethod, ABC


class BasePerception(ABC):

    @abstractmethod
    def getOG(agentLocation: Tuple[int, int], gridSize: Tuple[int, int], objects: List[BaseObject]) -> List[List[float]]:
        raise NotImplementedError("Please Implement this method")