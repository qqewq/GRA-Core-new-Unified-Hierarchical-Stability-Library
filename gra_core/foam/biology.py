import numpy as np
from .base import BaseFoam

class BiologyFoam(BaseFoam):
    """Пена биологического состояния: отклонение от гомеостаза."""
    def compute(self, state, context=None):
        if context is None:
            return np.sum(state**2)
        target = context.get('homeostasis', np.zeros_like(state))
        weights = context.get('weights', np.ones_like(state))
        diff = state - target
        return np.sum(weights * diff**2)

    def grad(self, state, context=None):
        if context is None:
            return 2 * state
        target = context.get('homeostasis', np.zeros_like(state))
        weights = context.get('weights', np.ones_like(state))
        return 2 * weights * (state - target)
