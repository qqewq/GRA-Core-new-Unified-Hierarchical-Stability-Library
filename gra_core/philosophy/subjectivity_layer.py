import numpy as np
from ..foam.subjectivity import SubjectivityFoam

def subjectivity_foam(state, self_model=None, dissonance_matrix=None):
    foam = SubjectivityFoam()
    ctx = {'self_model': self_model if self_model is not None else state,
           'dissonance_matrix': dissonance_matrix}
    return foam.compute(state, ctx)
