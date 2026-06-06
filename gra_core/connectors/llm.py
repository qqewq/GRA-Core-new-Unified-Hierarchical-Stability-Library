import numpy as np
class LLMConnector:
    def __init__(self, model_name): self.model = model_name
    def get_embedding(self, text):
        return np.random.randn(768)
