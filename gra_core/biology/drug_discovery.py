import numpy as np
from ..foam.biology import BiologyFoam

def drug_target_score(disease_state, target_state, foam_metric=None):
    if foam_metric is None:
        foam_metric = BiologyFoam()
    before = foam_metric.compute(disease_state)
    after = foam_metric.compute(target_state)
    return before - after
