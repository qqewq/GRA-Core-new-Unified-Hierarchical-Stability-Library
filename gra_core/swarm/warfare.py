import numpy as np
from ..foam.drone import DroneFoam

class WarfareDroneFoam(DroneFoam):
    """Расширенная пена войны: вражеские позиции и цели."""
    def compute(self, state, context=None):
        base = super().compute(state, context)
        if context is None:
            return base
        if 'enemy_positions' in context:
            er = context.get('engagement_range', 1.0)
            for ep in context['enemy_positions']:
                dist = np.linalg.norm(state - ep)
                if dist < er:
                    base += (er - dist)**2
        if 'mission_targets' in context:
            for t in context['mission_targets']:
                d = np.linalg.norm(state - t)
                base -= np.exp(-d)
        return max(0.0, base)
