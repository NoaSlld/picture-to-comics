import numpy as np

def convertir_en_gris(image_rgb):
    r = image_rgb[..., 0]
    g = image_rgb[..., 1]
    b = image_rgb[..., 2]

    # Appliquer les coefficients pour obtenir l'intensité en niveaux de gris
    gris = (0.2989 * r + 0.5870 * g + 0.1140 * b).astype(np.uint8)

    return gris
