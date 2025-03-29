# Projet Ver MAC - Hackathon 2025

<h1 align="center">
  <a href="https://github.com/TheBeesness/project_ver_mac">
    <img src="../docs/images/logo.png" alt="Logo" width="100" height="100">
  </a>
</h1>

<div align="center">
   🐝📸⚜️ <b>Hackathon 2025 - Projet Ver MAC</b> 🐝📸⚜️
  <br />
  <a href="#à-propos"><strong>Explorez les captures d'écran »</strong></a>
  <br />
  <br />
  <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Signaler un bug</a>
  ·
  <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Demander une fonctionnalité</a>
  ·
  <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Poser une question</a>
</div>

---

## Table des matières

- [À propos](#à-propos)
  - [Technologies utilisées](#technologies-utilisées)
- [Prise en main](#prise-en-main)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
- [Utilisation](#utilisation)
- [Vue d'ensemble des outils de surveillance](#vue-densemble-des-outils-de-surveillance)
- [Feuille de route](#feuille-de-route)
- [Support](#support)
- [Contribuer](#contribuer)
- [Auteurs et contributeurs](#auteurs-et-contributeurs)
- [Sécurité](#sécurité)
- [Remerciements](#remerciements)

## À propos

Le projet **Ver MAC** a été développé dans le cadre du Hackathon 2025 à Québec ⚜️, organisé par **l'initiative Mon Avenir TI de Québec International**. Le défi était de concevoir un programme capable d'estimer la durée de vie d'une batterie à partir de données collectées.

<details>
<summary>Captures d'écran</summary>
<br>
🛠️ **Processus d'installation**  
<img src="../docs/images/installation.png" alt="installation">

🎨 **Frontend en fonctionnement**  
<img src="../docs/images/using.png" alt="frontend_running">

📊 **Métriques affichées sur l'interface Web**  
<img src="../docs/images/url_frontend.png" alt="metrics_web">

🐳 **Vue d'ensemble des containers Docker**  
<img src="../docs/images/containers.png" alt="docker_containers">

⚙️ **Vue de la configuration Docker**  
<img src="../docs/images/config_view.png" alt="docker_config">

🎯 **Cibles Prometheus**  
<img src="../docs/images/target_prometheus.png" alt="prometheus_targets">

🔍 **Requêtes dans Prometheus**  
<img src="../docs/images/request_prometheus.png" alt="prometheus_query">

📊 **Dashboard Grafana**  
<img src="../docs/images/gafana.png" alt="grafana_dashboard">

🚨 **Interface AlertManager**  
<img src="../docs/images/alertmanager.png" alt="alertmanager">
</details>

### Technologies utilisées

- **Python 3.12**
- **UV**
- **Pip**
- **Prometheus_client**
- **Docker**
- **Grafana**

## Prise en main

### Prérequis

Pour travailler sur ce projet, vous devez avoir :

- **UV installé** (dans votre environnement virtuel `.venv`)
- **Prometheus_client installé** (pour la collecte de métriques)
- **Docker installé** (pour le déploiement en conteneurs)

### Installation

#### Configuration du backend

1. Ouvrez votre **terminal**.
2. Installez `uv` (dans votre environnement virtuel) :
   ```sh
   scoop install uv
   ```
3. Installez Flask :
   ```sh
   pip install Flask
   ```
4. Installez la bibliothèque Prometheus client :
   ```sh
   uv pip install prometheus_client
   ```
5. Lancez le programme :
   ```sh
   python main.py
   ```
6. Accédez au serveur web :
   ```sh
   http://localhost:8000/metrics
   ```

#### Configuration du frontend

1. Allez dans le répertoire :
   ```sh
   cd vermac-projet-hackathon-2025/prepa/promfun/prometheus
   ```
2. Démarrez les containers Docker :
   ```sh
   docker compose up -d
   ```
3. Accédez aux outils de surveillance :
   - **Prometheus** : [http://localhost:9090/](http://localhost:9090/)
   - **Grafana** : [http://localhost:3000/](http://localhost:3000/)
   - **AlertManager** : [http://localhost:9093/](http://localhost:9093/)

## Utilisation

### Backend

1. Dans `main.py`, définissez le chemin vers le fichier `.json` contenant les données de batterie.
   - Attention : Le dossier `Dataset\wetransfer\data` contient plusieurs fichiers JSON. Assurez-vous de spécifier celui que vous souhaitez utiliser.
2. Exécutez le programme :
   ```sh
   python main.py
   ```
3. Le programme traitera la dernière entrée de données et calculera le **State of Health (SOH)**.
4. La valeur SOH sera stockée et exposée via le serveur web sur le port **8000**.
5. Vérifiez les métriques traitées :
   ```sh
   http://localhost:8000/metrics
   ```

### Frontend

1. Installez **Docker Desktop** : [Site Web Docker](https://www.docker.com/)
2. Allez dans le répertoire du frontend :
   ```sh
   cd frontend
   ```
3. Démarrez les containers :
   ```sh
   docker compose up -d
   ```
4. Accédez aux outils de surveillance :
   - **Prometheus** : [http://localhost:9090/](http://localhost:9090/)
   - **Grafana** : [http://localhost:3000/](http://localhost:3000/)
   - **AlertManager** : [http://localhost:9093/](http://localhost:9093/)

## Vue d'ensemble des outils de surveillance

### Prometheus
Prometheus est un puissant outil open-source de surveillance et d'alerte conçu pour la fiabilité et l'évolutivité. Il collecte les métriques depuis les cibles configurées à intervalles réguliers, évalue des expressions de règles, affiche les résultats et déclenche des alertes si certaines conditions sont remplies.

### Grafana
Grafana est une plateforme open-source pour la surveillance et l'observabilité. Elle propose des visualisations interactives, des tableaux de bord personnalisables et des intégrations avec de multiples sources de données, y compris Prometheus, pour faciliter l'analyse en temps réel des données.

### AlertManager
AlertManager gère les alertes envoyées par Prometheus. Il s'occupe de la déduplication des alertes, du groupement, de la mise en sourdine et de l'envoi des notifications par email, Slack ou d'autres canaux. Il garantit une gestion efficace des incidents et des réponses dans un environnement de production.

## Feuille de route

Consultez les [problèmes ouverts](https://github.com/TheBeesness/project_ver_mac/issues) pour les fonctionnalités à venir et les problèmes connus.

- [Demandes de fonctionnalités](https://github.com/TheBeesness/project_ver_mac/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc)
- [Bugs majeurs](https://github.com/TheBeesness/project_ver_mac/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc)
- [Bugs les plus récents](https://github.com/TheBeesness/project_ver_mac/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

Si vous avez besoin de plus de support, n'hésitez pas à nous contacter.

## Contribuer

Veuillez lire nos [directives de contribution](docs/CONTRIBUTING.md) avant de soumettre des pull requests ou des problèmes.

## Auteurs et contributeurs

Le projet Ver MAC a été développé par l'**équipe centrale de Beesness**.

Consultez la liste complète des contributeurs sur [GitHub](https://github.com/TheBeesness/project_ver_mac/contributors).

## Sécurité

Le projet Ver MAC suit de bonnes pratiques de sécurité, mais une sécurité absolue ne peut être garantie. Utilisez-le à vos risques et périls.

Pour toute question de sécurité, consultez notre [documentation sur la sécurité](docs/SECURITY.md).

## Remerciements

Un grand merci à **Québec International** pour l'organisation du Hackathon 2025 et pour cette opportunité d'innover.

---

Cette traduction conserve la structure originale du README tout en l'adaptant à un public francophone. Si tu souhaites apporter d'autres modifications ou précisions, n'hésite pas à me le faire savoir !
