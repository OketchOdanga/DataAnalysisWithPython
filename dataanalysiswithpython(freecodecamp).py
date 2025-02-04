# -*- coding: utf-8 -*-
"""DataAnalysisWithPython(FreeCodecamp).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gA0Gfe6K8WCjb8UjLG5L4HyzTplf4zOE
"""

import sys
import numpy as np

np.array([1,2,3,4])

"""### Dimesions and Shapes"""

A = np.array([[1,3,4],[5,7,9]])
A

A.shape

A.ndim

A.size

B = np.array([
    [[2,3,4],[5,6,7]],
     [[8,9,0],[7,1,3]]
    ])
B

B.shape

B.ndim

B.size

A[1]

A[0]

#(x,y)
A[1][0]# element in the second row first column.

"""###Analysis"""

A.mean()

B.mean()

AB = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
])
AB

print(AB[:, :2])

