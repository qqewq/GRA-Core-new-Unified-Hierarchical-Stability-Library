import numpy as np

def love_oriented_nullify(state, context, foam_metric, lr=0.05):
    grad_self = foam_metric.grad(state, context)
    neighbor_grad = np.zeros_like(state)
    if 'neighbor_states' in context:
        for n_state in context['neighbor_states']:
            neighbor_grad += (state - n_state)
    total_grad = grad_self + 0.3 * neighbor_grad
    return state - lr * total_grad
