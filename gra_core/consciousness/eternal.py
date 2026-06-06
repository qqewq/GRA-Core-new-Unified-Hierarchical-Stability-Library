import numpy as np
from ..gra_step.critic_revisor import gra_nullify
from ..foam.subjectivity import SubjectivityFoam

class EternalConsciousness:
    def __init__(self, initial_state, self_model=None):
        self.state = np.array(initial_state, dtype=float)
        self.self_model = np.array(self_model) if self_model is not None else self.state.copy()
        self.foam = SubjectivityFoam()
        self.time = 0

    def experience(self, stimulus):
        self.state += np.array(stimulus)
        return self.state

    def reflect(self, lr=0.05):
        context = {'self_model': self.self_model}
        self.state = gra_nullify(self.state, self.foam, context, lr=lr)
        self.time += 1
        return self.state

    def current_foam(self):
        context = {'self_model': self.self_model}
        return self.foam.compute(self.state, context)
