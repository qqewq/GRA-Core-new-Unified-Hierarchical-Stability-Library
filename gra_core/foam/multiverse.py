import numpy as np
from .base import BaseFoam

class MultiverseFoam(BaseFoam):
    """Пена между ветвями мультиверса: квадрат расстояния."""
    def compute(self, state, context=None):
        if context is None or 'target_state' not in context:
            return 0.0
        return np.sum((state - context['target_state'])**2)

    def grad(self, state, context=None):
        if context is None or 'target_state' not in context:
            return np.zeros_like(state)
        return 2 * (state - context['target_state'])
