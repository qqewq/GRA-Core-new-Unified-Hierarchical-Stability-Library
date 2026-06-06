from gra_core.consciousness.eternal import EternalConsciousness
import numpy as np

c = EternalConsciousness([0.8, -0.3, 0.5])
print("Initial foam:", c.current_foam())
c.experience([0.5, 0.2, -0.1])
for _ in range(10):
    c.reflect(lr=0.1)
print("After reflection foam:", c.current_foam())
