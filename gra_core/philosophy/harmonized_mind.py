from ..optimizer.core import HierarchicalOptimizer
from ..hierarchy.level import Level
from ..foam.subjectivity import SubjectivityFoam

def harmonized_mind_step(levels, contexts, lr=0.01):
    foam = SubjectivityFoam()
    opt = HierarchicalOptimizer(levels, foam, alpha=[1.0]*len(levels), lr=lr)
    opt.step()
    return levels
