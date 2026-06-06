import numpy as np
from ..foam.base import BaseFoam
from ..gra_step.critic_revisor import gra_nullify

class CinemaNulling:
    def __init__(self, scenes, foam_metric: BaseFoam):
        self.scenes = [np.array(s, dtype=float) for s in scenes]
        self.foam = foam_metric
        self.history = []

    def nullify_scene(self, scene_idx, target_context, lr=0.1):
        if scene_idx < 0 or scene_idx >= len(self.scenes):
            raise IndexError("scene_idx out of range")
        old = self.scenes[scene_idx].copy()
        new = gra_nullify(self.scenes[scene_idx], self.foam, target_context, lr=lr)
        self.scenes[scene_idx] = new
        self.history.append(('nullify', scene_idx, old, new))
        return new

    def montage(self, sequence, context_sequence):
        for i in range(len(sequence)):
            if i < len(context_sequence):
                self.nullify_scene(sequence[i], context_sequence[i])
