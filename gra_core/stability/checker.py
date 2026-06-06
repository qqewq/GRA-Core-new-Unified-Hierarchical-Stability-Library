import numpy as np

def check_stability(levels, foam_metrics, tol=1e-6):
    L = len(levels)
    foams = [fm.compute(lvl.state, lvl.context) for lvl, fm in zip(levels, foam_metrics)]
    if any(f > tol for f in foams):
        return False
    dPhi = [foams[i+1]-foams[i] for i in range(L-1)]
    if any(abs(d) > tol for d in dPhi):
        return False
    for i in range(L-2):
        d2 = foams[i+2] - 2*foams[i+1] + foams[i]
        if d2 <= -tol:
            return False
    return True
