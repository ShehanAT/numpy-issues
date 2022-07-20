(numpy-dev) sean@sean-VirtualBox:~/Documents/PythonApplications/numpy$ python
Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np 
>>> from numpy.polynomial import Polynomial 
>>> Polynomial([np.inf]) / 2
Polynomial([inf], domain=[-1.,  1.], window=[-1.,  1.], symbol='x')



(numpy-dev) sean@sean-VirtualBox:~/Documents/PythonApplications/numpy$ python
Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np 
>>> from numpy.polynomial import Polynomial 
>>> Polynomial([np.inf]) / 2
/home/sean/Documents/PythonApplications/numpy/numpy/polynomial/polynomial.py:411: RuntimeWarning: invalid value encountered in multiply
  return c1/c2[-1], c1[:1]*0
Polynomial([inf], domain=[-1.,  1.], window=[-1.,  1.], symbol='x')