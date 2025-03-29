<!-- LOGO DU PROJET -->
<br />
<div align="center">
  <a href="https://github.com/majeurbilly/project_name">
    <img src="images/logo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Hackathon 2025 🦆</h3>

  <p align="center">
    Projet Ver-MAC
    <br />
    <a href="#a-propos"><strong>Explorer les captures d'écran »</strong></a>
      <br />
      <br />
      <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Signaler un bug</a>
      ·
      <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Demander une fonctionnalité</a>
      ·
      <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Poser une question</a>
  </p>
</div>

## Table des matières

- [À propos](#a-propos)
  - [Construit avec](#construit-avec)
- [Démarrage](#demarrage)
  - [Prérequis](#prerequis)
  - [Installation](#installation)
- [Utilisation](#utilisation)
- [Aperçu des outils de surveillance](#aperçu-des-outils-de-surveillance)
- [Auteurs & Contributeurs](#auteurs--contributeurs)
- [Remerciements](#remerciements)

## À propos

Le projet **Project Name** est un modèle de fichier README réutilisable, créé en mars 2025 à Québec ⚜️.

Description complète du **prochain projet**.

<details>
<summary>
  <img src="images/button.png" alt="bouton image" height=40> 
</summary>
<br>
🛠️ Processus d'installation  
<img src="images/installation.png" alt="installation">

🎨 Exécution du frontend  
<img src="images/using.png" alt="frontend_running">

📊 Affichage des métriques sur l'interface web  
<img src="images/url_frontend.png" alt="metrics_web">

🐳 Vue d'ensemble des conteneurs Docker  
<img src="images/containers.png" alt="docker_containers">

⚙️ Configuration Docker  
<img src="images/config_view.png" alt="docker_config">

🎯 Cibles Prometheus  
<img src="images/target_prometheus.png" alt="prometheus_targets">

🔍 Requête de métriques dans Prometheus  
<img src="images/request_prometheus.png" alt="prometheus_query">

📊 Tableau de bord Grafana  
<img src="images/gafana.png" alt="grafana_dashboard">

🚨 Interface AlertManager  
<img src="images/alertmanager.png" alt="alertmanager">
</details>

### Construit avec

- **Python 3.12**
- **UV**
- **Pip**
- **Prometheus_client**
- **Docker**
- **Grafana**

## Démarrage

### Prérequis

Pour utiliser ce projet, vous devez avoir :

- **UV installé** (dans votre environnement virtuel `.venv`)
- **Prometheus_client installé** (pour la collecte des métriques)
- **Docker installé** (pour le déploiement en conteneurs)

### Installation

#### Configuration du Backend

1. Ouvrir votre **terminal**.
2. Installer `uv` (dans l'environnement virtuel) :
   ```sh
   scoop install uv
   ```
3. Installer Flask :
   ```sh
   pip install Flask
   ```
4. Installer la bibliothèque Prometheus :
   ```sh
   uv pip install prometheus_client
   ```
5. Exécuter le programme :
   ```sh
   python main.py
   ```
6. Accès au serveur web :
   ```sh
   http://localhost:8000/metrics
   ```

#### Configuration du Frontend

1. Naviguer vers le répertoire :
   ```sh
   cd vermac-projet-hackathon-2025/prepa/promfun/prometheus
   ```
2. Démarrer les conteneurs Docker :
   ```sh
   docker compose up -d
   ```
3. Accéder aux outils web :
   - **Prometheus** : [http://localhost:9090/](http://localhost:9090/)
   - **Grafana** : [http://localhost:3000/](http://localhost:3000/)
   - **AlertManager** : [http://localhost:9093/](http://localhost:9093/)

## Utilisation

### Backend

1. Dans `main.py`, définir le chemin du fichier `.json` contenant les données de la batterie.
2. Exécuter :
   ```sh
   python main.py
   ```
3. Le programme analysera les données et calculera la métrique **State of Health (SOH)**.
4. La valeur SOH est stockée et accessible via le serveur web sur le port **8000**.
5. Vérifier les métriques traitées :
   ```sh
   http://localhost:8000/metrics
   ```

### Frontend

1. Installer **Docker Desktop** : [Docker Website](https://www.docker.com/)
2. Naviguer vers le répertoire du frontend :
   ```sh
   cd frontend
   ```
3. Démarrer les conteneurs :
   ```sh
   docker compose up -d
   ```
4. Accéder aux outils de surveillance :
   - **Prometheus** : [http://localhost:9090/](http://localhost:9090/)
   - **Grafana** : [http://localhost:3000/](http://localhost:3000/)
   - **AlertManager** : [http://localhost:9093/](http://localhost:9093/)

## Aperçu des outils de surveillance

### Prometheus
Prometheus est un outil open-source de surveillance et d'alerte conçu pour la fiabilité et l'évolutivité. Il collecte des métriques, évalue des règles et déclenche des alertes en cas d'anomalie.

### Grafana
Grafana est une plateforme open-source pour la visualisation des données. Elle permet de créer des tableaux de bord interactifs intégrant Prometheus et d'autres sources de données.

### AlertManager
AlertManager gère les alertes envoyées par Prometheus, en assurant la déduplication, le regroupement et l'envoi de notifications (email, Slack, etc.).

## Auteurs & Contributeurs

Le projet Ver-MAC a été développé par l'équipe #8.

## Remerciements

Merci à :

- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)

<p align="right">(<a href="#readme-top">Retour en haut</a>)</p>
