import numpy as np
import matplotlib.pyplot as plt
import random

head_tails=[0,0]
for _ in range(100000):
    head_tails[random.randint(0,1)]+=1
    plt.bar(["Heads", "Tails"],head_tails, color=["red","blue"])
    plt.pause(0.001)
    
    
plt.show()