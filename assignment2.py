import matplotlib.pyplot as plt
import numpy as np

class ProbabilityDensityFunction:
    ''''''
    def __init__(self,x,y):
        '''Constructor
        '''
        super().__init__(x, y)


if __name__ == '__main__':
    x = np.linspace(0., np.pi,20)
    y = np.sin(x)
    f = ProbabilityDensityFunction(x,y)

    plt.plot(x, y, 'o')
    _x = np.linspace(0., np.pi, 200)
    plt.plot(_x, f(_x))
    plt.show()