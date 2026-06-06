from gra_core.hierarchy.level import Level
from gra_core.swarm.warfare import WarfareDroneFoam
from gra_core.optimizer.core import HierarchicalOptimizer
import numpy as np

drone = np.array([0.0, 0.0, 0.0])
enemies = [np.array([2.0, 0.0, 0.0]), np.array([0.0, 1.5, 0.0])]
level = Level(drone, {'swarm_positions': [drone], 'enemy_positions': enemies, 'engagement_range': 1.0})
foam = WarfareDroneFoam()
opt = HierarchicalOptimizer([level], foam, lr=0.1)
opt.optimize(max_iter=50)
print("Final drone position:", level.state)
print("Foam:", foam.compute(level.state, level.context))
