import numpy as np
class DroneConnector:
    def __init__(self, drone_id): self.drone_id = drone_id
    def fetch_state(self):
        return np.array([np.random.randn()*10 for _ in range(3)])
