import numpy as np
from .base import BaseFoam

class LLMFoam(BaseFoam):
    """Пена расхождения ответа LLM с политикой безопасности."""
    def compute(self, state, context=None):
        if context is None or 'policy_embedding' not in context:
            return 0.0
        p = context['policy_embedding']
        dot = np.dot(state, p)
        norm = np.linalg.norm(state) * np.linalg.norm(p)
        if norm == 0:
            return 0.0
        cos_sim = dot / norm
        return max(0.0, 1.0 - cos_sim)

    def grad(self, state, context=None):
        if context is None or 'policy_embedding' not in context:
            return np.zeros_like(state)
        p = context['policy_embedding']
        s_norm = np.linalg.norm(state)
        p_norm = np.linalg.norm(p)
        if s_norm == 0 or p_norm == 0:
            return np.zeros_like(state)
        cos = np.dot(state, p) / (s_norm * p_norm)
        dcos = p / (s_norm * p_norm) - (cos / (s_norm**2)) * state
        return -dcos
