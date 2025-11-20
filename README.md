# Génération du Rapport PFE (RoSiStrat)

## HTML enrichi
Le fichier `rapport.html` contient le rapport structuré avec :
- Table des matières avec liens et pagination approximative
- Placeholders d'images au format demandé
- Extraits de code minimisés
- Bouton de téléchargement PDF (impression côté navigateur)

## Génération PDF serveur (Puppeteer)
Installation :
```bash
npm install
```

Générer le PDF :
```bash
npm run pdf
```
Le fichier `rapport.pdf` sera produit à la racine.

## Ajout d'images
Placez vos images selon les dossiers suggérés (ex: `images/architecture/diagram.png`). Intégrez-les ensuite en remplaçant les blocs placeholder dans `rapport.html`.

## Limite de pages
Le contenu est conçu pour rester ≤ 60 pages A4 (dépend du nombre et taille des images). Optimisez les images (compression, résolution 150–200 DPI).
# lapage