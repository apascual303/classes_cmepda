#ABOUT THE 2nd ASSIGNMENT

'''Unit test for the pdf
'''

from gettext import npgettext
import unittest
import sys

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

if sys.flags.interactive:
    plt.ion()

from splrand.pdf import ProbabilityDensityFunction

class TestPdf (unittest.TestCase):
    '''
    '''

    def __init__ (self, x, y, k = 3):
        '''Constructor.
        '''
        norm = InterpolatedUnivariateSpline(x, y, k = k).integral(x[0], x[-1])
        y /= norm
        super().__init__(x, y)
        ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x])
        self.cdf = InterpolatedUnivariateSpline(x, ycdf)
        xppf, ippf = np.unique(ycdf, return_index = True)
        yppf = x[ippf]
        self.ppf = InterpolatedUnivariateSpline(xppf, yppf, k = k)



    def test_uniform(test):
        '''
        '''
        x = np.linspace(0., 1., 100)
        y = np.full(x.shape, 1.)
        pdf = ProbabilityDensityFunction(x, y)
        #print(x, y)
        #plt.plot(x, y)
        print(pdf)
        #print(pdf(0.5))
        self.assertAlmostEqual(pdf(0.5), 1.)
        self.assertAlmostEqual(pdf.integral(0.,1.), 1.)
        self.assertAlmostEqual(pdf.prob(0.25, 0.75), 0.5)
    
    def test_triangular(self):
        x = np.linspace(0., 1., 100)
        y = 2.* x
        pdf = ProbabilityDensityFunction(x, y)
        plt.figure('Triangular pdf')
        plt.plot(x, pdf(x))
        plt.figure('Triangular cdf')
        plt.plot(x, pdf.cdf(x))
        plt.figure('Triangular ppf')
        plt.plot(x, pdf.ppf(x))
        plt.show()

        r = pdf.rnd(1000000)
        plt.figure('Triangular random variate')
        plt.hist(r, bins=200)

    def test_fancy(self):
        '''
        '''
        x = np.linspace(0., 1., 100)
        y = np.zeros(x.shape)
        y[x <= 0.5] = 2. * x[x <= 0.5]
        y[x > 0.75] = 3.
        plt.figure('Fancy pdf')
        xgrid = np.linspace(0., 1., 1000)
        plt.plot(xgrid, pdf(xgrid))
        plt.plot(x, pdf(x))
        print(pdf.integral(0., 1.))
    

if __name__ == '__main__':
    unittest.main(exit=not sys.flags.interactive)




###############################################################################################


