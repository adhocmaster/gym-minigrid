import gym

from gym_minigrid.agents.PedAgent import PedAgent

# creating env
env = gym.make('Crosswalk-Empty-20x80-v0')
env.reset()

# creating agents
agents = []
agents.append(PedAgent(0, (1, 1), 2))
agents.append(PedAgent(1, (3, 2), 2))

# adding agents to env
env.addAgents(agents)
