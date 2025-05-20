import numpy as np

 # Calculate the angle between two vectors given positions in nonEuclidean space
def calculateSpectralAngle(spectralArray1, spectralArray2):
    angle = np.arccos( (np.dot(spectralArray1, spectralArray2)) / (np.linalg.norm(spectralArray1)*(np.linalg.norm(spectralArray2))))

    angleDeg = angle * (180.0/np.pi)
    print('The Spectral Angle in radians is: ');
    print(angle)

    print('The Spectral Angle in degrees is: ');
    print(angleDeg)

    return angle, angleDeg