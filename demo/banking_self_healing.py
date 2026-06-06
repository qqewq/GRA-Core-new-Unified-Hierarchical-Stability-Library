import numpy as np
from gra_core.hierarchy.level import Level
from gra_core.foam.banking import BankingFoam
from gra_core.optimizer.core import HierarchicalOptimizer
from gra_core.stability.perturbation import perturbation_test

levels = [
    Level(np.array([6.0, 2.0]), {'limits': np.array([5.0, 5.0])}),
    Level(np.array([12.0]), {'limits': np.array([10.0])}),
    Level(np.array([15.0]), {'limits': np.array([20.0])})
]
foam = BankingFoam()
opt = HierarchicalOptimizer(levels, foam, alpha=[1,0.5,0.1], lr=0.1)
opt.optimize(max_iter=100)
print("Initial convergence. Levels:", [lvl.state for lvl in levels])
print("Perturbation test passed?", perturbation_test(opt, noise_scale=2.0))
