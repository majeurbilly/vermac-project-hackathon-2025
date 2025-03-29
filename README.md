<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/majeurbilly/project_name">
    <img src="docs/images/logo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Hackathon 2025 🦆</h3>

  <p align="center">
    Project Ver-MAC
    <br />
    <a href="#about"><strong>Explore the screenshots »</strong></a>
      <br />
      <br />
      <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
      ·
      <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
      ·
      <a href="https://github.com/TheBeesness/project_ver_mac/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
  </p>
</div>




  ## Table of Contents
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#monitoring-tools-overview">Monitoring Tools Overview</a></li>
    <li><a href="#authors--contributors">Authors & Contributors</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>




<!-- ABOUT THE PROJECT -->
## About
Project **Project Name** is a reusable project of readme template made in March 2025 in Quebec City ⚜️ 

Reste of description of **next project**



<details>
 <summary>
    <a href="#images">
      <img src="docs/images/button.png" alt="button image" height="40">
    </a>
<br>
  ### images
🛠️ Installation Process  
<img src="docs/images/installation.png" alt="installation">

🎨 Frontend Running  
<img src="docs/images/using.png" alt="frontend_running">

📊 Metrics Displayed on Web Interface  
<img src="docs/images/url_frontend.png" alt="metrics_web">

🐳 Docker Containers Overview  
<img src="docs/images/containers.png" alt="docker_containers">

⚙️ Docker Configuration View  
<img src="docs/images/config_view.png" alt="docker_config">

🎯 Prometheus Targets  
<img src="docs/images/target_prometheus.png" alt="prometheus_targets">

🔍 Querying Metrics in Prometheus  
<img src="docs/images/request_prometheus.png" alt="prometheus_query">

📊 Grafana Dashboard  
<img src="docs/images/gafana.png" alt="grafana_dashboard">

🚨 AlertManager Interface  
<img src="docs/images/alertmanager.png" alt="alertmanager">
</details>

### Built With

- **Python 3.12**
- **UV**
- **Pip**
- **Prometheus_client**
- **Docker**
- **Grafana**

## Getting Started

### Prerequisites

To work with this project, you need to have:

- **UV installed** (inside your virtual environment `.venv`)
- **Prometheus_client installed** (for metric collection)
- **Docker installed** (for containerized deployment)

### Installation

#### Backend Setup

1. Open your **terminal**.
2. Install `uv` (inside your virtual environment):
   ```sh
   scoop install uv
   ```
3. Install Flask:
   ```sh
   pip install Flask
   ```
4. Install Prometheus client library:
   ```sh
   uv pip install prometheus_client
   ```
5. Run the program:
   ```sh
   python main.py
   ```
6. Web server access:
   ```sh
   http://localhost:8000/metrics
   ```

#### Frontend Setup

1. Navigate to:
   ```sh
   cd vermac-projet-hackathon-2025/prepa/promfun/prometheus
   ```
2. Start Docker containers:
   ```sh
   docker compose up -d
   ```
3. Web access:
   - **Prometheus**: [http://localhost:9090/](http://localhost:9090/)
   - **Grafana**: [http://localhost:3000/](http://localhost:3000/)
   - **AlertManager**: [http://localhost:9093/](http://localhost:9093/)

## Usage

### Backend

1. In `main.py`, set the path to the `.json` file containing the battery data.
2. Run:
   ```sh
   python main.py
   ```
3. The program will process the latest data entry and compute the **State of Health (SOH)** metric.
4. The SOH value is stored and exposed via the web server on port **8000**.
5. Check the processed metrics:
   ```sh
   http://localhost:8000/metrics
   ```

### Frontend

1. Install **Docker Desktop**: [Docker Website](https://www.docker.com/)
2. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
3. Start the containers:
   ```sh
   docker compose up -d
   ```
4. Access monitoring tools:
   - **Prometheus**: [http://localhost:9090/](http://localhost:9090/)
   - **Grafana**: [http://localhost:3000/](http://localhost:3000/)
   - **AlertManager**: [http://localhost:9093/](http://localhost:9093/)

## Monitoring Tools Overview

### Prometheus
Prometheus is a powerful open-source monitoring and alerting toolkit designed for reliability and scalability. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays results, and triggers alerts if certain conditions are met.

### Grafana
Grafana is an open-source platform for monitoring and observability. It provides interactive visualizations, customizable dashboards, and integrations with multiple data sources, including Prometheus, to facilitate real-time data analysis.

### AlertManager
AlertManager handles alerts sent by Prometheus. It manages alert deduplication, grouping, silencing, and sending notifications via email, Slack, or other channels. It ensures efficient incident management and response in a production environment.

## Authors & Contributors

Project Ver MAC was developed by the team #8

## Acknowledgments

Remerciment:

* [Prometheus](https://prometheus.io/)
* [Grafana](https://grafana.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


