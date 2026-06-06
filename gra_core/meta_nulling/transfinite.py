import numpy as np

class TransfiniteCore:
    def __init__(self, foam, gra_step_fn):
        self.foam = foam
        self.gra_step = gra_step_fn

    def transfinite_nullify(self, initial_state, context, max_steps=1000, omega_steps=10):
        state = initial_state
        for ordinal in range(omega_steps):
            old = state.copy()
            for _ in range(max_steps):
                state = self.gra_step(state, self.foam, context)
                if np.linalg.norm(state - old) < 1e-10:
                    break
                old = state.copy()
            state += 1e-6 * np.random.randn(*state.shape)
        return state
