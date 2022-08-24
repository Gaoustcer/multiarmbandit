from mutiarmbandit import K

from random import random

sigma = []
mu = []
EXTEND = 128
for i in range(K):
    mu.append(EXTEND * random())
    sigma.append(EXTEND * random())
    # randomfunctionlist.append(normal.Normal(mu[i],sigma[i]))
import numpy as np

np.save('mu.npy',np.array(mu))
np.save('sigma.npy',np.array(sigma))
