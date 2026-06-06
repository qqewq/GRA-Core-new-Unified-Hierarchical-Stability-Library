from gra_core.swarm.warfare import WarfareDroneFoam
import numpy as np

def test_warfare():
    foam = WarfareDroneFoam()
    state = np.array([0.0, 0.0, 0.0])
    ctx = {'swarm_positions': [state], 'enemy_positions': [np.array([0.5, 0.0, 0.0])],
           'engagement_range': 1.0}
    f = foam.compute(state, ctx)
    assert f >= 0
