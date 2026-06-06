import numpy as np
from ..foam.base import BaseFoam

def cell_twin_sync(real_cell_state, digital_twin_state, foam_metric: BaseFoam, lr=0.01):
    diff = real_cell_state - digital_twin_state
    grad = foam_metric.grad(diff)
    return digital_twin_state - lr * grad
