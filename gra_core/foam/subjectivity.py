import numpy as np
from .base import BaseFoam

class SubjectivityFoam(BaseFoam):
    """Пена субъективности: мера внутренней противоречивости агента."""
    def compute(self, state, context=None):
        if context is None:
            return 0.0
        self_model = context.get('self_model', state)
        base = np.sum((state - self_model)**2)
        if 'dissonance_matrix' in context:
            D = context['dissonance_matrix']
            base += np.sum(D * np.outer(state, state))
        return base

    def grad(self, state, context=None):
        if context is None:
            return np.zeros_like(state)
        self_model = context.get('self_model', state)
        grad = 2 * (state - self_model)
        if 'dissonance_matrix' in context:
            D = context['dissonance_matrix']
            grad += (D + D.T) @ state
        return grad
