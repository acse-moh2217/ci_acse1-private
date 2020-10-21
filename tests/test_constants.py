import numpy as np

from simple_functions import pi
from simple_functions import mysin


class TestPi(object):
    '''Class to test our constants are computed correctly'''

    def test_pi(self):
        '''Test computation of pi'''
        my_pi = pi(1)
        assert np.isclose(my_pi, np.pi, atol=1e-12)

    def test_mysin(self):
        mymysin=mysin(30, 5)
        assert np.isclose(mymysin, np.sin(30), atol=1e-4)