import numpy as np

def linear_data_sample(N=40, rseed=0, m=3, b=-2):
    rng = np.random.RandomState(rseed)

    x = 10 * rng.rand(N)
    dy = m / 2 * (1 + rng.rand(N))
    y = m * x + b + dy * rng.randn(N)

    return (x, y, dy)
    
