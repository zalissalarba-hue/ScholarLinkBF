# Projet

## objectif du projet

Créer une plateforme numérique qui centralise et gère les opportunités de :

Bourses d’études

Stages académiques et professionnels

👉 Le but est d’aider les étudiants et jeunes professionnels du Burkina Faso et de la région Ouest‑Africaine à trouver et suivre les opportunité de bourses et de stage facilement.

## Technologies utilisées

- Frontrend
  - Flutter
- Backend
  - Flask (pour l'api)
  - Scraping: BeautifulSoup pour extraire automatiquement les informations sur les bourses et stages depuis des sites externes
- Base de données
  - PostgreSQL pour stocker les offres et les candidatures

## Fonctionnalités principales

  Gestion des utilisateurs

      Inscription / connexion
 
      Profils étudiants avec informations académiques

  Catalogue d’opportunités

      Liste des bourses disponibles

      Liste des stages disponibles

      Recherche et filtres (par domaine, pays, niveau d’études, etc.)

  Scraping & mise à jour

      Extraction automatique des nouvelles offres

      Mise à jour régulière de la base de données

  Notifications & alertes

      Informer les utilisateurs des nouvelles opportunités correspondant à leur profil

## Interface utilisateur

  Accueil : présentation du projet et navigation simple

  Panneau latéral (sidebar) : accès rapide aux bourses et stages 

  Tableaux de bord : suivi personnalisé des opportunités

## Rapport du projet


## Dépendance du projet

```bash
conda create --name env-scholarlinkbf python==3.12
conda activate env-scholarlinkbf
```
