import numpy as np

#calculating Eigen values, Eigen vectors, and the Coefficient Matrix for a matrix
def matrixMath(matrix):
    eigenValues, eigenVectors = np.linalg.eig(matrix)

    print('The eigenvalues of the covariance matrix are: ')
    print(eigenValues)

    print('The eigenvectors for covariance matrix are: ')
    print(eigenVectors)

    coefficentMatrix = eigenVectors.transpose()
    print('The coefficient matrix is: ')
    print(coefficentMatrix)

    return eigenValues, eigenVectors, coefficentMatrix

#calculate mean of matrix
def matrixMean(matrix):
    mean = np.mean(matrix)
    return mean

#calculate principal components of matrix values and arrays of x,y coordinates
def principalComponents(matrix, array1, array2):
    mean = matrixMean(matrix)
    eigenVal, eigenVectors, coefficientmatrix = matrixMath(matrix)

    pcArray1 = np.matmul(coefficientmatrix, (array1-mean))
    pcArray2 = np.matmul(coefficientmatrix, (array2-mean))    
    
    print('The Principal Component transformed value for array1 is: ');
    print(pcArray1)  

    print('The Principal Component transformed value for array2 is: ');
    print(pcArray2)

    return pcArray1, pcArray2