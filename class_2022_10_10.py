import numpy as np

a = np.linspace(1.,10.,10)
b = np.full(10,3.)

#I can do:
a*b

c = np.array([3,4])

#I can't do:
'''
a*c
'''
#There's a ValueError

#to do the scalar product between a and b:
(a*b).sum()
np.sum(a*b)


#Rules of Broadcasting
a = np.array([[1.,2.],[3.,4.]])
b=np.array([2.,2.])

a*b

################


import random
import numpy as np
import matplotlib.pyplot as plt

N = 1000000
lambda_ = 0.1 #micro metros  ---- the underscore is because 'lambda' already exists in python basic variables
THICKNESS = 0.200 # micro m
num_absorbed = 0.

def eff_simple (num_events):
    abs_z = []
    t0 = time.time()
    for i in range(num_events):     ### FOR are very 'expensive' in the time sense in python, we have to avoid them
        z = random.expovariate(1. / lambda_)
        abs_z.append(z)
        if z < THICKNESS:
            num_absorbed += 1

    elapsed_time = time.time() - t0
    print('Running time: {elapsed_time} s')
    return abs_z

def eff_vectorized(num_events):
    abs_z = np.random.exponential(lambda_, size = num_events)
    print(abs_z)
    abs_z = abs_z[abs_z <= THICKNESS] #we use the mask and then recreate the abs_z as the array of the elements that follow the condition of the maskara
    return abs_z

'''
z = eff_simple(N)
quantum_efficiency = len(z) / N
'''

z = eff_vectorized(N)


quantum_efficiency = num_absorbed / N
print(f'Quantum efficiency: {quantum_efficiency}')

plt.hist(abs_z, bins = 100)
plt.yscale('log')
plt.show()
