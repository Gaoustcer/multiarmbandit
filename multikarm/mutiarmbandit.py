from torch.distributions import normal
from random import random
from random import randint
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm
writer = SummaryWriter('./log/randomchoice')
K = 10
testtimes = 512

epsilon = 0.1
ITERTIME = 128
# mu = []
# sigma = []
randomfunctionlist = []
import numpy as np

mu = np.load('mu.npy')
sigma = np.load('sigma.npy')
for i in range(K):
    # mu.append(random())
    # sigma.append(random())
    randomfunctionlist.append(normal.Normal(mu[i],sigma[i]))
# import numpy as np

# np.save('mu.npy',np.array(mu))
# np.save('sigma.npy',np.array(sigma))

def randomchoice():
    index = randint(0,K-1)
    return randomfunctionlist[index].sample()
decisionlist = {}
for i in range(K):
    decisionlist[i] = {'reward':0,'times':1,'averagereward':0}
def epsilon_algorithm():
    if random() < epsilon:
        action = randint(0,K-1)
    else:
        action = -1
        averagereward = -1
        for i in range(K):
            if averagereward < decisionlist[i]['averagereward']:
                averagereward = decisionlist[i]['averagereward']
                action = i
        pass
    reward = randomfunctionlist[action].sample()
    decisionlist[action]['reward'] += reward

    decisionlist[action]['times'] += 1
    decisionlist[action]['averagereward'] = decisionlist[action]['reward'] / decisionlist[action]['times']
    return reward
    pass
if __name__ == "__main__":
    for i in tqdm(range(ITERTIME)):
        reward = 0
        for _ in range(testtimes):
            reward += randomchoice()
        writer.add_scalar('reward',reward/testtimes,i)