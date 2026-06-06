from gra_core.heisenberg.reasoning import HeisenbergReasoner
import numpy as np

def test_heisenberg_foam():
    hr = HeisenbergReasoner(h=1.0)
    state = np.array([1.0, 0.5])
    assert hr.foam(state) >= 0
