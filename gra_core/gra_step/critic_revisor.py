import numpy as np

def gra_nullify(state, foam_metric, context, max_inner_iter=5, lr=0.1):
    current = state.copy()
    original_foam = foam_metric.compute(current, context)
    for _ in range(max_inner_iter):
        grad = foam_metric.grad(current, context)
        if 'projection' in context:
            low, high = context['projection']
            current = np.clip(current - lr * grad, low, high)
        else:
            current -= lr * grad
        new_foam = foam_metric.compute(current, context)
        if new_foam < original_foam:
            break
        lr *= 0.5
    return current
