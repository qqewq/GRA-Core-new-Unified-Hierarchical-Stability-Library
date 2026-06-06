import numpy as np
from .base import BaseFoam

class BankingFoam(BaseFoam):
    """Пена как сумма квадратов превышения лимитов."""
    def compute(self, state, context=None):
        if context is None:
            return np.sum(np.maximum(0, state)**2)
        limits = context.get('limits', np.zeros_like(state))
        over = np.maximum(0, state - limits)
        return np.sum(over**2)

    def grad(self, state, context=None):
        if context is None:
            return 2 * np.maximum(0, state)
        limits = context.get('limits', np.zeros_like(state))
        over = np.maximum(0, state - limits)
        return 2 * over * (state > limits)
