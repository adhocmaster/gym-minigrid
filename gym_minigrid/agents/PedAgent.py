from gym_minigrid.agents.Agent import Agent
from gym_minigrid.agents import Lanes
import numpy as np

class PedAgent(Agent):
    # [0] = x axis [1] = y-axis
    # 1 = down face
    # 3 = up face
    def parallel1InterspersedFlow(self, agents):
        #TODO Simulate lane change
        gaps = np.zeros((3, 3)).astype(int)
        gaps[1] = [-1, -1, -1]
        gaps[2] = [-1, -1, -1]
        gaps[0] = self.computeGapInterspersedFlow(agents, Lanes.currentLane)
        if self.canShiftLeft == True:
            gaps[1] = self.computeGapInterspersedFlow(agents, Lanes.leftLane)
        if self.canShiftRight == True:
            gaps[2] = self.computeGapInterspersedFlow(agents, Lanes.rightLane)
        
        # print('gaps', gaps)
        # confused about DML(Dynamic Multiple Lanes)
        maxGap = 0
        for i in range(3):
            maxGap = max(maxGap, gaps[i][0])
        # print('maxgap', maxGap)
        goodLanes = []
        for i in range(3):
            if maxGap == gaps[i][0]:
                goodLanes.append(i)
        
        if len(goodLanes) == 1:
            lane = goodLanes[0]
        elif len(goodLanes) == 2:
            if goodLanes[0] == Lanes.currentLane:
                if np.random.random() > 0.2:
                    lane = goodLanes[0]
                else:
                    lane = goodLanes[1]
            else: #no current lane
                if np.random.random() > 0.5:
                    lane = goodLanes[0]
                else:
                    lane = goodLanes[1]
        else:
            prob = np.random.random()
            if prob > 0.2:
                lane = goodLanes[0]
            elif prob > 0.1:
                lane = goodLanes[1]
            else:
                lane = goodLanes[2]

        self.speed = gaps[lane][0]
        self.gapSame = gaps[lane][1]
        self.gapOpp = gaps[lane][2]

        return lane
        pass
        
    def parallel1DMLFlow(self, agents):
        #TODO Simulate lane change
        gaps = np.zeros((3, 3)).astype(int)
        gaps[0] = self.computeGapDML(agents, Lanes.currentLane)
        if self.canShiftLeft == True:
            gaps[1] = self.computeGapDML(agents, Lanes.leftLane)
        if self.canShiftRight == True:
            gaps[2] = self.computeGapDML(agents, Lanes.rightLane)
        
        # print('gaps', gaps)
        # confused about DML(Dynamic Multiple Lanes)
        maxGap = 0
        for i in range(3):
            maxGap = max(maxGap, gaps[i][0])
        # print('maxgap', maxGap)
        goodLanes = []
        for i in range(3):
            if maxGap == gaps[i][0]:
                goodLanes.append(i)
        
        if len(goodLanes) == 1:
            lane = goodLanes[0]
        elif len(goodLanes) == 2:
            if goodLanes[0] == Lanes.currentLane:
                if np.random.random() > 0.2:
                    lane = goodLanes[0]
                else:
                    lane = goodLanes[1]
            else: #no current lane
                if np.random.random() > 0.5:
                    lane = goodLanes[0]
                else:
                    lane = goodLanes[1]
        else:
            prob = np.random.random()
            if prob > 0.2:
                lane = goodLanes[0]
            elif prob > 0.1:
                lane = goodLanes[1]
            else:
                lane = goodLanes[2]

        self.speed = gaps[lane][0]
        self.gapSame = gaps[lane][1]
        self.gapOpp = gaps[lane][2]

        return lane
        pass
        

    def parallel2(self, agents):
        #TODO What lane allows agent to move using max speed
        if self.speed == self.gapOpp and self.speed < 2 and self.direction == 2: # might be wrong
            posX, posY = self.position
            for agent in agents:
                
                if posY == agent.position[1] and agent.direction == 0 and (posX - agent.position[0]) <= 2*(self.speed + 1) and (posX - agent.position[0] > 0):
                    print('found match', self.position, agent.position, self.speed, agent.speed)
                    if self.exchangeProbability >= np.random.random():
                        self.speed = self.speed + 1
                        agent.speed += 1
                    else:
                        self.speed = 0
                        agent.speed = 0

        pass

    def computeGapInterspersedFlow(self, agents, lane):
        """
        Compute the gap (basically the possible speed ) according to the paper
        """
        # first sameGap
        postionX = self.position[0]
        postionY = self.position[1]
        gap_opposite = 4
        gap_same = 8
        if lane == Lanes.leftLane:
            postionY -= 1
        elif lane == Lanes.rightLane:
            postionY += 1
        for agent2 in agents:
            #sameGap, so direction must be same and they must be in same lane
            if self.direction != agent2.direction or postionY != agent2.position[1]: 
                continue
            if self.direction == 2: #looking up
                gap = postionX - agent2.position[0]
                if gap > 0 and gap <= 8: # gap must not be negative and less than 8
                    gap_same = min(gap_same, gap - 1)
            elif self.direction == 0: #looking down
                gap = agent2.position[0] - postionX
                if gap > 0 and gap <= 8: # gap must not be negative and less than 8
                    gap_same = min(gap_same, gap - 1)

                    

        # now oppGap
        for agent2 in agents:
            #oppGap, so direction must be different and they must be in same lane
            if self.direction == agent2.direction or postionY != agent2.position[1]: 
                continue
            if self.direction == 2: #looking up
                gap = postionX - agent2.position[0]
                if gap > 0 and gap <= 8: # gap must not be negative and less than 4
                    gap_opposite = min(gap_opposite, (gap-1)/2)
            elif self.direction == 0: #looking down
                gap = agent2.position[0] - postionX
                if gap > 0 and gap <= 8: # gap must not be negative and less than 4
                    gap_opposite = min(gap_opposite, (gap-1)/2)

        gap = min(self.initSpeed, min(gap_same, gap_opposite))
        return gap, gap_same, gap_opposite
        
    def computeGapDML(self, agents, lane):
        """
        Compute the gap (basically the possible speed ) according to the paper
        """
        # first sameGap
        postionX = self.position[0]
        postionY = self.position[1]
        gap_opposite = 4
        gap_same = 8
        if lane == Lanes.leftLane:
            postionY -= 1
        elif lane == Lanes.rightLane:
            postionY += 1
        for agent2 in agents:
            #sameGap, so direction must be same and they must be in same lane
            if self.direction != agent2.direction or postionY != agent2.position[1]: 
                continue
            if self.direction == 2: #looking up
                gap = postionX - agent2.position[0]
                if gap > 0 and gap <= 8: # gap must not be negative and less than 8
                    gap_same = min(gap_same, gap)
            elif self.direction == 0: #looking down
                gap = agent2.position[0] - postionX
                if gap > 0 and gap <= 8: # gap must not be negative and less than 8
                    gap_same = min(gap_same, gap)

                    

        # now oppGap
        for agent2 in agents:
            #oppGap, so direction must be different and they must be in same lane
            if self.direction == agent2.direction or postionY != agent2.position[1]: 
                continue
            if self.direction == 2: #looking up
                gap = postionX - agent2.position[0]
                if gap > 0 and gap <= 8: # gap must not be negative and less than 4
                    gap_opposite = 0
            elif self.direction == 0: #looking down
                gap = agent2.position[0] - postionX
                if gap > 0 and gap <= 8: # gap must not be negative and less than 4
                    gap_opposite = 0

        gap = min(self.initSpeed, min(gap_same, gap_opposite))
        return gap, gap_same, gap_opposite
        

   

from enum import IntEnum

class Lanes(IntEnum):
    currentLane = 0
    leftLane = 1
    rightLane = 2