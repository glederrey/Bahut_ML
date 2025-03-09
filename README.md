# Bahut_ML
Exercices pour le cours de Machine Learning du Bahut

## Description
Bienvenue chez **AeroAnalytics**, une startup spécialisée dans l'analyse de données pour l'industrie aéronautique !

En tant que nouvelle recrue dans notre équipe de Data Science, vous allez relever deux défis majeurs qui aideront notre entreprise à se positionner comme leader dans le secteur :

### Mission 1 : Amélioration de l'expérience client
Notre client principal, une compagnie aérienne internationale, souhaite améliorer la satisfaction de ses passagers. Ils nous ont fourni des données d'enquêtes de satisfaction et nous demandent de développer un modèle prédictif capable d'identifier les passagers susceptibles d'être insatisfaits avant même qu'ils ne descendent de l'avion. Cela permettra à la compagnie d'intervenir de manière proactive pour résoudre les problèmes.

Votre mission : Construire un modèle de classification performant qui prédit si un passager sera satisfait ou non de son vol en fonction de diverses caractéristiques et métriques de service.

### Mission 2 : Optimisation des stratégies tarifaires
Notre deuxième client, une agence de voyage en ligne, cherche à optimiser ses stratégies de tarification et à offrir des prévisions de prix précises à ses utilisateurs. Ils nous ont fourni des données historiques de prix de billets d'avion entre plusieurs grandes villes américaines.

Votre mission : Développer un modèle de régression capable de prédire le prix des billets d'avion en fonction de différents paramètres (date, compagnie, itinéraire, etc.), permettant ainsi à l'agence de conseiller ses clients sur le meilleur moment pour acheter leurs billets.

Au cours de ce programme de formation accélérée, vous apprendrez à manipuler des données réelles, à construire des modèles de machine learning performants et à communiquer efficacement vos résultats. Chaque jour apportera de nouveaux défis et compétences qui vous aideront à devenir un data scientist accompli chez AeroAnalytics !

Êtes-vous prêt à décoller vers le succès ?

## Structure du dépôt
- `exercices/` : Contient les notebooks Jupyter pour chaque jour
- `data/` : Contient les jeux de données utilisés dans les exercices
- `corrections/` : Contient les corrections des exercices

## Configuration de l'environnement

### Prérequis
- [Anaconda](https://www.anaconda.com/download/) ou [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (pour l'option conda)
- Python 3.13 ou supérieur

### Option 1 : Création de l'environnement conda
Suivez ces étapes pour configurer l'environnement de travail avec conda :

1. Ouvrez un terminal (ou Anaconda Prompt sous Windows)
2. Créez un nouvel environnement conda avec Python 3.13 :
   ```bash
   conda create -n bahut_ml python=3.13
   ```
3. Activez l'environnement :
   ```bash
   conda activate bahut_ml
   ```
4. Installez les dépendances avec uv :
   ```bash
   python -m pip install -r requirements.txt
   ```

### Option 2 : Utilisation de uv avec venv
Si vous préférez utiliser venv au lieu de conda :

1. Ouvrez un terminal
2. Créez un environnement virtuel avec Python 3.13 :
   ```bash
   python -m venv bahut_ml_env
   ```
3. Activez l'environnement :
   - Sur Linux/macOS :
     ```bash
     source bahut_ml_env/bin/activate
     ```
   - Sur Windows :
     ```bash
     bahut_ml_env\Scripts\activate
     ```
4. Installez les dépendances avec uv :
   ```bash
   uv pip install -r requirements.txt
   ```

## Contenu du cours

### Jour 1 : Fondamentaux - Chargement et visualisation des données
- Exercice 1 : Introduction à Pandas
- Exercice 2 : Visualisation des données avec Plotly
- Exercice 3 : Transformation des données

### Jour 2 : Manipulation de données et premiers modèles de ML
- Exercice 1 : Pandas avancé
- Exercice 2 : Ingénierie des caractéristiques
- Exercice 3 : Premier modèle de classification

### Jour 3 : Amélioration des modèles et régression
- Exercice 1 : Amélioration de la classification
- Exercice 2 : Introduction à la régression
- Exercice 3 : Visualisation des résultats des modèles

### Jour 4 : Différents parcours d'apprentissage
- Exercices guidés combinant tous les concepts précédents
- Construction d'un pipeline ML complet
- Débogage des erreurs courantes dans les workflows ML