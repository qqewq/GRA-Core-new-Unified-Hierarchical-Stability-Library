import numpy as np
from ..foam.subjectivity import SubjectivityFoam

def intersubjectivity_foam(state_a, state_b, self_models=None):
    foam = SubjectivityFoam()
    ctx_a = {'self_model': self_models[0] if self_models else state_a}
    ctx_b = {'self_model': self_models[1] if self_models else state_b}
    return (foam.compute(state_a, ctx_a) +
            foam.compute(state_b, ctx_b) +
            np.sum((state_a - state_b)**2))
