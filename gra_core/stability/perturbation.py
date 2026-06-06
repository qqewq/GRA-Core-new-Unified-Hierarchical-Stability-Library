import numpy as np
from .checker import check_stability

def perturbation_test(optimizer, noise_scale=0.1, recovery_steps=50):
    for lvl in optimizer.levels:
        lvl.state += noise_scale * np.random.randn(*lvl.state.shape)
    for _ in range(recovery_steps):
        optimizer.step()
    return check_stability(optimizer.levels, optimizer.foam_metrics)
