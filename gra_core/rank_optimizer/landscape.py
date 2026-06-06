import numpy as np
from ..optimizer.core import HierarchicalOptimizer

def find_optimal_rank(levels, foam_metrics, max_rank=10, max_iter=100, lr=0.01):
    best_foam = float('inf')
    best_rank = len(levels)
    for rank in range(1, min(max_rank, len(levels))+1):
        sub_levels = [lvl.copy() for lvl in levels[:rank]]
        sub_foams = foam_metrics[:rank] if isinstance(foam_metrics, list) else [foam_metrics]*rank
        opt = HierarchicalOptimizer(sub_levels, sub_foams, lr=lr)
        opt.optimize(max_iter=max_iter, check_every=max_iter)
        total_foam = sum(fm.compute(lvl.state, lvl.context) for fm, lvl in zip(sub_foams, sub_levels))
        if total_foam < best_foam:
            best_foam = total_foam
            best_rank = rank
    return best_rank
