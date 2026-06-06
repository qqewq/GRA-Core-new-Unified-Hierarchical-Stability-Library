import numpy as np

class Level:
    def __init__(self, state: np.ndarray, context: dict = None):
        self.state = state.astype(float)
        self.context = context or {}

    def foam(self, foam_metric):
        return foam_metric.compute(self.state, self.context)

    def copy(self):
        return Level(self.state.copy(), self.context.copy())
