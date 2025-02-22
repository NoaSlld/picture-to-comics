import os
from src.charger_sauvegarder import charger_image, afficher_et_sauvegarder
from src.niveaux_de_gris import convertir_en_gris
from src.detection_contours import detecter_contours
from src.reduction_fusion import reduire_couleurs, fusionner_images
from src.steps import etapes_traitement_image


# Chemins des dossiers
dossier_images = "img"
dossier_sortie = "resultats"

# Création du dossier de sortie s'il n'existe pas
os.makedirs(dossier_sortie, exist_ok=True)

# Filtrer uniquement les fichiers d'images dans le dossier
extensions_autorisees = {".jpg", ".jpeg", ".png", ".bmp"}
images_a_traiter = [f for f in os.listdir(dossier_images) if os.path.splitext(f)[1].lower() in extensions_autorisees]


# Boucle sur chaque image
for nom_image in images_a_traiter:
    chemin_entree = os.path.join(dossier_images, nom_image)
    chemin_sortie = os.path.join(dossier_sortie, f"comics_{nom_image}")

    print(f"Traitement de {nom_image}...")

    # Charger l’image
    image_rgb = charger_image(chemin_entree)

    # Convertir en niveaux de gris
    image_gris = convertir_en_gris(image_rgb)

    # Détection des contours
    contours = detecter_contours(image_gris, seuil=50)

    # Réduction des couleurs
    image_reduite = reduire_couleurs(image_rgb, k=8)

    # Fusionner les contours avec l'image réduite
    image_finale = fusionner_images(image_reduite, contours)

    # Sauvegarde
    afficher_et_sauvegarder(image_finale, chemin_sortie)

    print(f"Image enregistrée : {chemin_sortie}")


# etapes_traitement_image("./img/chateau.jpg")