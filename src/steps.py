import os
from src.charger_sauvegarder import charger_image, afficher_et_sauvegarder
from src.niveaux_de_gris import convertir_en_gris
from src.detection_contours import detecter_contours
from src.reduction_fusion import reduire_couleurs, fusionner_images


# Traite une seule image et enregistre chaque étape du traitement
def etapes_traitement_image(chemin_entree, dossier_sortie="./steps"):

    os.makedirs(dossier_sortie, exist_ok=True)
    nom_image = os.path.basename(chemin_entree)
    nom_base = os.path.splitext(nom_image)[0]
    
    print(f"Traitement de {nom_image}...")

    # Charger l’image
    image_rgb = charger_image(chemin_entree)
    
    # Convertir en niveaux de gris
    image_gris = convertir_en_gris(image_rgb)
    chemin_gris = os.path.join(dossier_sortie, f"{nom_base}_gris.png")
    afficher_et_sauvegarder(image_gris, chemin_gris)
    
    # Détection des contours
    contours = detecter_contours(image_gris, seuil=50)
    chemin_contours = os.path.join(dossier_sortie, f"{nom_base}_contours.png")
    afficher_et_sauvegarder(contours, chemin_contours)
    
    # Réduction des couleurs
    image_reduite = reduire_couleurs(image_rgb, k=8)
    chemin_reduit = os.path.join(dossier_sortie, f"{nom_base}_reduit.png")
    afficher_et_sauvegarder(image_reduite, chemin_reduit)
    
    # Fusionner les contours avec l'image réduite
    image_finale = fusionner_images(image_reduite, contours)
    chemin_sortie = os.path.join(dossier_sortie, f"{nom_base}_final.png")
    afficher_et_sauvegarder(image_finale, chemin_sortie)
    
    print(f"Images enregistrées dans {dossier_sortie}.")
