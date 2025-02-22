from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def charger_image(chemin):
    image = Image.open(chemin).convert("RGB")
    return np.array(image)



def afficher_et_sauvegarder(image_array, chemin_sortie):
    image = Image.fromarray(image_array)
    image.save(chemin_sortie)

    plt.imshow(image)
    plt.axis("off")
    plt.show()

