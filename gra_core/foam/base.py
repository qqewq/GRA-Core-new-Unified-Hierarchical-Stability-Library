import numpy as np

class BaseFoam:
    """Абстрактная метрика пены Φ: X × Context → R⁺"""
    def compute(self, state: np.ndarray, context: dict = None) -> float:
        raise NotImplementedError
    def grad(self, state: np.ndarray, context: dict = None) -> np.ndarray:
        raise NotImplementedError
