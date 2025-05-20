import numpy as np

#calculating distance between two points
#points are np.arrays containing x and y coordinates only
#must exist within the same "space"

def calcEuclideanDist(x1, x2):
    ed = np.sqrt(np.matmul(np.matrix.transpose(x1-x2),(x1-x2)))
    print('The Euclidean distance is: ')
    print(ed)