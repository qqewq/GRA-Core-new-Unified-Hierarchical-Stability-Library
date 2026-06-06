import numpy as np
from ..foam.biology import BiologyFoam
from ..optimizer.core import HierarchicalOptimizer
from ..hierarchy.level import Level

def health_swarm_optimize(patient_biomarkers, homeostasis, swarm_size=5, lr=0.05):
    foam = BiologyFoam()
    agents = [Level(homeostasis + 0.1*np.random.randn(*homeostasis.shape),
                     {'homeostasis': homeostasis}) for _ in range(swarm_size)]
    for _ in range(50):
        for ag in agents:
            opt = HierarchicalOptimizer([ag], foam, lr=lr)
            opt.step()
        foams = [foam.compute(ag.state, ag.context) for ag in agents]
        best_idx = np.argmin(foams)
        best_state = agents[best_idx].state
        for ag in agents:
            ag.state += 0.1 * (best_state - ag.state)
    return agents
