import numpy as np

class ASIMetricSpace:
    def __init__(self, foam_metric):
        self.foam_metric = foam_metric
    def distance(self, state_a, state_b, context=None):
        diff = state_a - state_b
        return self.foam_metric.compute(diff, context)
