import numpy as np

#calculating Eigen values, Eigen vectors, and the Coefficient Matrix for a matrix
def matrixMath(valA1, valA2, valB1, valB2):
    matrix = np.array([[valA1, valA2], [valB1, valB2]], dtype=float)

    eigenValues, eigenVectors = np.linalg.eig(matrix)

    print('The eigenvalues of the covariance matrix are: ')
    print(eigenValues)

    print('The eigenvectors for covariance matrix are: ')
    print(eigenVectors)

    coefficentMatrix = eigenVectors.transpose()
    print('The coefficient matrix is: ')
    print(coefficentMatrix)