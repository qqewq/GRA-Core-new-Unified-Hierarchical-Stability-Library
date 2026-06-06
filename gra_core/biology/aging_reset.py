import numpy as np
from ..foam.biology import BiologyFoam
from ..gra_step.critic_revisor import gra_nullify

def aging_reset_step(biomarkers, homeostasis, lr=0.05):
    foam = BiologyFoam()
    context = {'homeostasis': homeostasis}
    return gra_nullify(biomarkers, foam, context, lr=lr)
