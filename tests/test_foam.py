from gra_core.foam.banking import BankingFoam
import numpy as np

def test_banking_foam():
    foam = BankingFoam()
    state = np.array([0.0, 0.0])
    assert foam.compute(state, {'limits': np.array([1.0, 1.0])}) == 0.0
