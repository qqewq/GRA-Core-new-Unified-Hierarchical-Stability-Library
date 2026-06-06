import numpy as np
def emotional_state_update(current_emotion, stimulus, lr=0.1):
    return (1 - lr) * current_emotion + lr * stimulus
