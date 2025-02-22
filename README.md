# Projet_Comics

Projet de traitement d'image réalisé seul en une petite dizaine de jours lors de ma troisième année de BUT. 

Objectif: transformer une photo existante en style "Comics"

## Utilisation: 
Pour tester avec vos propres images, veuillez les inserer dans le dossier "/img" du projet. 
Ensuite, lancez le script 'main.py'. # Projet_Comics

**Image, Son et Visualisation: Projet de traitement d'image**

## Objectif :

Ce projet a pour but de transformer une photo classique en un effet "Comics". Grâce à une série de traitements d'image, nous appliquons des techniques de détection de contours, de réduction de couleurs et d'effets visuels pour obtenir une image stylisée qui imite l'apparence des dessins animés ou des bandes dessinées.

---

## Fonctionnalités principales :

- **Transformation en niveaux de gris :**  
  La conversion de l'image en noir et blanc permet de simplifier la détection des contours et d'éliminer les couleurs inutiles.
  
- **Détection des contours :**  
  Utilisation du filtre de Sobel pour détecter les bords et renforcer le contraste entre les éléments importants de l'image.

- **Réduction des couleurs :**  
  Utilisation du K-means pour réduire le nombre de couleurs de l'image, afin de créer un effet visuel "plat" et simplifié comme dans une BD.

- **Fusion des contours et des couleurs réduites :**  
  Les contours noirs sont superposés à l'image réduite en couleurs pour obtenir l'effet final.

---

## Prérequis :

- **Python 3.x**
- Les bibliothèques suivantes doivent être installées :
  - `numpy`
  - `scipy`
  - `sklearn`
  - `matplotlib` (optionnel, pour l'affichage)

Vous pouvez installer les dépendances via `pip` :

```bash
pip install numpy scipy scikit-learn matplotlib
```

---

## Utilisation :

### 1. Préparation de l'image :
Pour tester avec vos propres images, insérez-les dans le dossier `/img` du projet. Le programme supporte les formats suivants : `.jpg`, `.jpeg`, `.png`, `.bmp`.

### 2. Lancer le script :
Exécutez le script principal `main.py` pour appliquer l'effet Comics à toutes les images présentes dans le dossier `/img`.

```bash
python main.py
```

Le programme traitera chaque image et générera une version stylisée du fichier dans le dossier `/resultats`.

### 3. Sauvegarde des résultats :

Les images traitées seront sauvegardées avec un préfixe `comics_` et placées dans le dossier `/resultats`. Par exemple, si l'image d'entrée s'appelle `image.jpg`, l'image résultante sera nommée `comics_image.jpg`.



---

## Explication du traitement de l'image :


### 1. Chargement de l'image :

L'image est d'abord chargée en utilisant la fonction charger_image et convertie en un format RGB.

### 2. Conversion en niveaux de gris :

Le programme convertit l'image en niveaux de gris (une seule composante de couleur par pixel) afin de simplifier les calculs de détection des contours. Cela élimine les variations de couleur inutiles (comme les teintes similaires entre le rouge, le vert et le bleu), ce qui rend la détection des contours plus précise et plus rapide.

### 3. Détection des contours :

Le programme applique le filtre Sobel pour détecter les bords de l'image. Ce filtre calcule la variation d'intensité lumineuse dans l'image et met en évidence les zones de contraste élevé (les bords). Après la détection, un seuil est appliqué pour éliminer les contours faibles et inutiles, et une érosion binaire est utilisée pour affiner les contours.

### 4. Réduction des couleurs :

Une réduction des couleurs est effectuée en utilisant l'algorithme K-means clustering. Cet algorithme regroupe les pixels de l'image en un nombre réduit de couleurs (par défaut 8). Cela simplifie les détails de l'image et donne un effet de dessin animé avec des zones de couleur plates et uniformes.

### 5. Fusion des couleurs et des contours :

Enfin, les contours détectés (initialement noirs) sont superposés sur l'image réduite en couleurs pour ajouter des détails définis, typiques du style comics. Un léger flou est appliqué pour adoucir les contours et donner un effet plus naturel.
