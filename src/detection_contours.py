import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.ndimage import binary_erosion

# matrices de Sobel pour détecter les bords
sobel_x = np.array([[-1, 0, 1], 
                     [-2, 0, 2], 
                     [-1, 0, 1]])

sobel_y = np.array([[-1, -2, -1], 
                     [0,  0,  0], 
                     [1,  2,  1]])



# Applique une convolution 3x3 sur une image en niveaux de gris
def appliquer_filtre(image, kernel):
    # Récupère les dimensions de l'image
    hauteur, largeur = image.shape  

    # Initialise une image de sortie remplie de zéros avec les mêmes dimensions
    sortie = np.zeros((hauteur, largeur))  

    # Parcourt chaque pixel de l'image (en excluant les bords)
    for i in range(1, hauteur - 1):  
        for j in range(1, largeur - 1):  
            # Extrait la région 3x3 autour du pixel actuel
            region = image[i - 1:i + 2, j - 1:j + 2]  

            # Convolution
            sortie[i, j] = np.sum(region * kernel)

    return sortie



# Détecte les contours d'une image en niveaux de gris en utilisant le filtre de Sobel et un seuil pour éliminer les détails
def detecter_contours(image_gris, seuil=80):

    # Appliquer un flou pour lisser les détails et éviter un excès de contours
    image_lisse = gaussian_filter(image_gris, sigma=1.5)

    # Filtre Sobel pour extraire les bords
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    grad_x = np.abs(appliquer_filtre(image_lisse, sobel_x))
    grad_y = np.abs(appliquer_filtre(image_lisse, sobel_y))

    contours = np.hypot(grad_x, grad_y)

    # Appliquer un seuil pour éviter trop de détails
    # (contours > seuil) vérifie pour chaque pixel si sa valeur est supérieure au seuil.
    # (contours > seuil) est de type "bool" et retourne une matrice où, pour chaque pixel il y a True ou False
    # Chaque valeur de Contours est donc égal à 0 ou 255
    contours_binaires = (contours > seuil)
    return binary_erosion(contours_binaires).astype(np.uint8) * 255