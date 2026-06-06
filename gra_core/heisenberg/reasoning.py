import numpy as np

class HeisenbergReasoner:
    def __init__(self, h=1.0):
        self.h = h

    def foam(self, state, context=None):
        x, p = state[0], state[1]
        base = x**2 + p**2
        violation = max(0.0, self.h/2 - abs(x) * abs(p))
        return base + violation

    def nullify(self, state, lr=0.05, steps=5):
        s = state.copy()
        for _ in range(steps):
            eps = 1e-6
            grad = np.zeros_like(s)
            for i in range(len(s)):
                sp = s.copy(); sp[i] += eps
                sm = s.copy(); sm[i] -= eps
                fp = self.foam(sp)
                fm = self.foam(sm)
                grad[i] = (fp - fm) / (2*eps)
            s -= lr * grad
        return s
