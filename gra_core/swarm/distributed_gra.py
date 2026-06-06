import numpy as np
from ..optimizer.core import HierarchicalOptimizer

class DistributedGRAOptimizer:
    def __init__(self, agents, lr=0.01):
        self.agents = agents
        self.lr = lr

    def step(self):
        positions = [agent.levels[0].state for agent in self.agents]
        for agent in self.agents:
            for lvl in agent.levels:
                lvl.context['swarm_positions'] = positions
            opt = HierarchicalOptimizer(
                levels=agent.levels,
                foam_metrics=agent.foam_metrics,
                lr=self.lr)
            opt.step()
