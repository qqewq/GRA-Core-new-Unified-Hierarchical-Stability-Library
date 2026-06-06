import numpy as np
from .base import BaseFoam

class DroneFoam(BaseFoam):
    """Пена конфликтов роя: штраф за нарушение безопасного расстояния."""
    def compute(self, state, context=None):
        if context is None or 'swarm_positions' not in context:
            return 0.0
        positions = context['swarm_positions']
        safe_radius = context.get('safe_radius', 1.0)
        dists = [np.linalg.norm(state - p) for p in positions if not np.array_equal(p, state)]
        if not dists:
            return 0.0
        violation = max(0.0, safe_radius - min(dists))
        return violation**2

    def grad(self, state, context=None):
        eps = 1e-6
        grad = np.zeros_like(state)
        for i in range(len(state)):
            s_plus = state.copy(); s_plus[i] += eps
            s_minus = state.copy(); s_minus[i] -= eps
            f_plus = self.compute(s_plus, context)
            f_minus = self.compute(s_minus, context)
            grad[i] = (f_plus - f_minus) / (2*eps)
        return grad
