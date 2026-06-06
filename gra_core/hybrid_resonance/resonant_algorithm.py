import numpy as np

def hybrid_resonance_step(state, context, foam_metric, resonance_factor=0.3, lr=0.1):
    grad_foam = foam_metric.grad(state, context)
    attractors = context.get('attractors', [])
    if attractors:
        dists = [np.linalg.norm(state - a) for a in attractors]
        nearest = attractors[np.argmin(dists)]
        resonance_grad = (nearest - state)
        total_step = -lr * grad_foam + resonance_factor * resonance_grad
    else:
        total_step = -lr * grad_foam
    return state + total_step
