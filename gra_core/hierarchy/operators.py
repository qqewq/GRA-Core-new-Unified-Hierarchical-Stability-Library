import numpy as np

def lift_operator(state_l, state_l1, config=None):
    if config is None or 'matrix' not in config:
        return state_l1
    return config['matrix'] @ state_l1

def connection_penalty(x_l, x_l1, A_config=None):
    A_x_l1 = lift_operator(x_l, x_l1, A_config)
    diff = x_l - A_x_l1
    return 0.5 * np.sum(diff**2)

def grad_connection_wrt_lower(x_l, x_l1, A_config=None):
    A_x_l1 = lift_operator(x_l, x_l1, A_config)
    return x_l - A_x_l1

def grad_connection_wrt_upper(x_l, x_l1, A_config=None):
    A_x_l1 = lift_operator(x_l, x_l1, A_config)
    diff = x_l - A_x_l1
    if A_config is None or 'matrix' not in A_config:
        return -diff
    return -A_config['matrix'].T @ diff
