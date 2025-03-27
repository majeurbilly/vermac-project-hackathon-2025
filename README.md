<h1 align="center">
  <a href="https://github.com/TheBeesness/project_name">
    <img src="docs/images/logo.png" alt="Logo" width="100" height="100">
  </a>
</h1>

<div align="center">
   🐝📸⚜️ <b>hackathon 2025 - Projet Ver MAC</b> 🐝📸⚜️
  <br />
  <a href="#about"><strong>Explore the screenshots »</strong></a>
  <br />
  <br />
  <a href="https://github.com/majeurbilly/projet_name/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/majeurbilly/projet_name/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/majeurbilly/projet_name/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
- [Project assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

<table><tr><td>

> **[📸]**
> <b>vermac-projet-hackathon-2025</b> is a competition in Quebec city ⚜️.
> Organized by Québec International's Mon Avenir TI initiative,
> the challenge was to design a program that could determine a battery's lifespan based on received data.

<details>
<summary>Screenshots</summary>
<br>

> **[?]**
> TODO: Actual Screenshots.

|                               Home Page                               |                               Login Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/screenshot.png" title="Home Page" width="100%"> | <img src="docs/images/screenshot.png" title="Login Page" width="100%"> |

</details>

</td></tr></table>

### Built With

> **[📸]**
> - Python 3.12
> - UV
> - Pip
> - Prometheus_client
> - Docker
> - Grafana
> - < Front End Stack >

## Getting Started

### Prerequisites

> **[📸]**
> To work with this project, you need to have uv installed (on your .venv) and installed prometheus_client (for use the lib).

### Installation

> **[📸]**
> Installation for backend development is made via terminal on your root repository.
> Go to the `terminal`
> `scoop install uv` for install uv in your .venv
> `pip install Flask` for use the library Flask
> `uv pip install prometheus_client` for use the library prometheus_client
> And `python .\main.py` for Run the program
> web server access :
  > web server http://localhost:8000/metrics
> Installation for frontend development
> Aller dans le dossier `vermac-projet-hackathon-2025\prepa\promfun\prometheus`
> Go to the `terminal`
> `docker compose up -d` pour partir le contenaire docker
> docker access:
  > Prometheus http://localhost:9090/
  > Grafana http://localhost:9093/   

## Usage

> **[📸]**
> backend
  > A la ligne 106 du programme ce trouve le chemin vers le fichier .json ou se trouve les données utile au calcul du SOH. Selectionné le fichier a tester en changeant ce string 
  > Suite a la commande python .\main.py executer dans le termial, celle-ci part le server web
  > Une fois que le programme roule celui-ce traite le fichier .json
  > le progamme selectionne la donnnée la plus recent en parcourant chaques données. cette donnée est stocké en variable au sain du programme pour calculé le SOH et est aussi envoyé en metric sur le pour 8000
> frontend
  > 

## Roadmap

See the [open issues](https://github.com/TheBeesness/project_name/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/TheBeesness/project_name/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/TheBeesness/project_name/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/TheBeesness/project_name/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

> **[📸]**
> Additional support is available upon request. Contact information should have been shared already.

## Project assistance

If you want to say **thank you** or/and support active development of <b>project_name</b>:

- Add a [GitHub Star](https://github.com/TheBeesness/project_name) to the project.
- Tweet about <b>project_name</b>.

## Contributing

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [Beesness Core Team](https://github.com/TheBeesness).

For a full list of all authors and contributors, see [the contributors page](https://github.com/TheBeesness/project_name/contributors).

## Security

<b>project_name</b> follows good practices of security, but 100% security cannot be assured.
<b>project_name</b> is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._


## Acknowledgements

> **[📸]**
> TODO
