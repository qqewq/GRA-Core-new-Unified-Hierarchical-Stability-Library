from ..hierarchy.level import Level

class SwarmAgent:
    def __init__(self, agent_id, levels, foam_metrics):
        self.id = agent_id
        self.levels = levels
        self.foam_metrics = foam_metrics
