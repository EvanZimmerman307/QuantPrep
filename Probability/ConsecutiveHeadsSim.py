import random
import numpy as np

required_heads = 3
results = []
for i in range(10000):
    heads_count = 0
    flip_count = 0
    
    while heads_count < 3:
        if random.choice(['H','T']) == 'H':
            heads_count += 1
        else:
            heads_count = 0
        
        flip_count += 1
    
    results.append(flip_count)

print(np.mean(results))

    