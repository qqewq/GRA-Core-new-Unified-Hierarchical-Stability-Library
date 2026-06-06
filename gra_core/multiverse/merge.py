import numpy as np
from ..hierarchy.level import Level
from ..optimizer.core import HierarchicalOptimizer
from ..foam.multiverse import MultiverseFoam

def merge_branches(branch_a, branch_b, lr=0.01):
    merged_levels = []
    for l in range(len(branch_a.levels)):
        avg = (branch_a.levels[l].state + branch_b.levels[l].state) / 2.0
        merged_levels.append(Level(avg, branch_a.levels[l].context))
    foam = MultiverseFoam()
    foams = [foam] * len(merged_levels)
    opt = HierarchicalOptimizer(merged_levels, foams, lr=lr)
    opt.optimize(max_iter=200)
    return merged_levels
