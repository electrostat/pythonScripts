import numpy as np

#The Adaptive Cosine Estimator (ACE) algorithm is a popular method used in hyperspectral image processing for target detection.
#It determines the presence of a specific material within a hyperspectral image by calculating the normalized correlation between the spectrum of each pixel and a known target spectrum.

def aceScoreCalculation(spectrumValA1, spectrumValA2, spectrumValB1, spectrumValB2):
    # Define the pixel spectrum and target spectrum
    pixel_spectrum = np.array([spectrumValA1, spectrumValA2])
    target_spectrum = np.array([spectrumValB1, spectrumValB2])

    # Calculate dot products
    numerator = np.dot(pixel_spectrum, target_spectrum)**2
    denominator = np.dot(pixel_spectrum, pixel_spectrum) * np.dot(target_spectrum, target_spectrum)

    # ACE score calculation
    ace_score = numerator / denominator
    print(f"ACE Score: {ace_score}")


