import numpy as np
from sklearn.cluster import KMeans
import cv2


# réduit le nombre de couleurs d'une image avec K-means clustering
def reduire_couleurs(image_rgb, k=8):

    pixels = image_rgb.reshape(-1, 3)  # Transformer en une liste de pixels
    
    # Coupe les valeurs très élevées pour éviter trop hautes lumières
    # pixels = np.clip(pixels, 0, 200)  # créer des tâches blanches sur le visage

    # Appliquer K-means pour classifier les pixels en k couleurs
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = kmeans.fit_predict(pixels)
    palette = kmeans.cluster_centers_.astype(np.uint8)

    # Remplacer chaque pixel par la couleur du centre de son cluster
    image_quantifiee = palette[labels].reshape(image_rgb.shape)

    return image_quantifiee


# Remplace les pixels blancs par les couleurs environnantes en utilisant une interpolation.
def remplacer_blanc_par_voisin(image):

    # Créer un masque pour les pixels blancs
    blanc_mask = np.all(image == [255, 255, 255], axis=-1)
    
    # Utiliser une technique de dilatation pour trouver les voisins proches
    dilate_mask = cv2.dilate(blanc_mask.astype(np.uint8), np.ones((5, 5), np.uint8), iterations=1)
    
    # Remplacer les pixels blancs par les pixels voisins (moyenne)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            if blanc_mask[i, j]:
                voisinage = image[i-1:i+2, j-1:j+2]
                couleur_voisine = np.mean(voisinage[~blanc_mask[i-1:i+2, j-1:j+2]], axis=0)
                image[i, j] = couleur_voisine

    return image


# Superpose les contours noirs sur l'image réduite en couleurs
def fusionner_images(image_couleurs, contours, alpha=0.8):
    contours_inverses = 255 - contours  # Inverser les contours (noir → blanc)
    
    # Appliquer un flou léger pour rendre les contours plus doux
    contours_filtres = np.clip(contours_inverses * alpha, 0, 255).astype(np.uint8)
    
    # Convertir en RGB pour superposer avec l’image
    contours_rgb = np.stack([contours_filtres] * 3, axis=-1)  
    
    # Mélanger contours et image avec un mode de fusion "darken"
    image_finale = np.minimum(image_couleurs, contours_rgb)
    
    # Remplacer les pixels blancs par les voisins
    image_finale = remplacer_blanc_par_voisin(image_finale)

    return image_finale
