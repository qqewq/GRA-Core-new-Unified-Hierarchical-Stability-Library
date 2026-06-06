import numpy as np
from ..hierarchy.operators import connection_penalty, grad_connection_wrt_lower, grad_connection_wrt_upper
from ..gra_step.critic_revisor import gra_nullify
from ..stability.checker import check_stability

class HierarchicalOptimizer:
    def __init__(self, levels, foam_metrics, alpha=None, beta=None, gamma=1.0,
                 A_configs=None, terminal_penalty_fn=None, lr=0.01):
        self.levels = levels
        if isinstance(foam_metrics, list):
            self.foam_metrics = foam_metrics
        else:
            self.foam_metrics = [foam_metrics] * len(levels)
        self.L = len(levels)
        self.alpha = alpha or [1.0]*self.L
        self.beta = beta or [1.0]*(self.L-1)
        self.gamma = gamma
        self.A_configs = A_configs or [None]*(self.L-1)
        self.terminal_penalty_fn = terminal_penalty_fn
        self.lr = lr

    def compute_J(self):
        J_val = 0.0
        for l in range(self.L):
            J_val += self.alpha[l] * self.foam_metrics[l].compute(
                self.levels[l].state, self.levels[l].context)
        for l in range(self.L-1):
            C = connection_penalty(self.levels[l].state, self.levels[l+1].state,
                                   self.A_configs[l])
            J_val += self.beta[l] * C
        if self.terminal_penalty_fn:
            J_val += self.gamma * self.terminal_penalty_fn(self.levels[-1].state)
        return J_val

    def step(self):
        # 1. GRA-обнуление
        for l in range(self.L):
            self.levels[l].state = gra_nullify(
                self.levels[l].state, self.foam_metrics[l], self.levels[l].context)
        # 2. градиентный спуск по J
        for l in range(self.L):
            grad = np.zeros_like(self.levels[l].state)
            grad += self.alpha[l] * self.foam_metrics[l].grad(
                self.levels[l].state, self.levels[l].context)
            if l < self.L-1:
                grad += self.beta[l] * grad_connection_wrt_lower(
                    self.levels[l].state, self.levels[l+1].state, self.A_configs[l])
            if l > 0:
                grad += self.beta[l-1] * grad_connection_wrt_upper(
                    self.levels[l-1].state, self.levels[l].state, self.A_configs[l-1])
            if self.terminal_penalty_fn and l == self.L-1:
                eps = 1e-6
                s = self.levels[l].state
                term_grad = np.zeros_like(s)
                for i in range(len(s)):
                    sp = s.copy(); sp[i] += eps
                    sm = s.copy(); sm[i] -= eps
                    fp = self.terminal_penalty_fn(sp)
                    fm = self.terminal_penalty_fn(sm)
                    term_grad[i] = (fp - fm) / (2*eps)
                grad += self.gamma * term_grad
            self.levels[l].state -= self.lr * grad

    def optimize(self, max_iter=1000, tol=1e-6, check_every=10):
        for it in range(max_iter):
            old_states = [lvl.state.copy() for lvl in self.levels]
            self.step()
            max_diff = max(
                np.max(np.abs(old_states[i] - self.levels[i].state))
                for i in range(self.L))
            if max_diff < tol and check_stability(self.levels, self.foam_metrics):
                print(f"Stability reached at iteration {it}")
                break
        return self.levels
