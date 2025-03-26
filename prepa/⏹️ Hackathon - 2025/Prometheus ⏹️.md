---
weeks_at_school: 24
days_at_school: 174
tags:
---
https://github.com/prometheus-community/windows_exporter


---

![[Pasted image 20250320210413.png]]

![[Pasted image 20250320210225.png]]

![[Pasted image 20250323014926.png]]

YAML

```
scrape_protocols:
  - OpenMetricsText1.0.0
  - OpenMetricsText0.0.1
  - PrometheusText0.0.4
```

Cela indique à Prometheus qu'il doit tenter de récupérer les métriques en utilisant ces formats, dans l'ordre indiqué.

- **`OpenMetricsText1.0.0` et `OpenMetricsText0.0.1`**: Ce sont des versions du format OpenMetrics, une norme ouverte pour l'exposition de métriques. OpenMetrics vise à standardiser la manière dont les métriques sont formatées, ce qui facilite l'interopérabilité entre différents systèmes de surveillance.
- **`PrometheusText0.0.4`**: C'est le format de texte original utilisé par Prometheus. Il est moins standardisé que OpenMetrics, mais il est toujours largement utilisé.

**Comment Prometheus utilise `scrape_protocols`**

Lorsque Prometheus récupère des métriques à partir d'une cible, il essaie d'abord d'utiliser le premier protocole spécifié dans `scrape_protocols`. Si cela réussit, il utilise ce format. Sinon, il essaie le protocole suivant, et ainsi de suite, jusqu'à ce qu'il trouve un format compatible ou qu'il ait essayé tous les protocoles.

---

![[Pasted image 20250323020309.png]]
**`up{job="<job-name>", instance="<instance-id>"}`**:

- C'est une métrique Prometheus qui indique si une instance est opérationnelle. Si la valeur de "up" est 1, cela signifie que l'instance est accessible et que Prometheus peut collecter ses métriques. Si la valeur est 0, cela signifie que l'instance est inaccessible.
- `up{instance="192.168.62.3:9100", job="node_exporter", service="myapp"}`:
    - Ceci est un exemple concret. Il indique que l'instance "192.168.62.3:9100" (qui fait partie du job "node_exporter" et est associée au service "myapp") est opérationnelle.
**Définitions : Métriques**

- **`ex : node_cpu_seconds_total{cpu="0", mode="iowait"} 0.3`**:
    - C'est un exemple de métrique Prometheus. Elle se compose du nom de la métrique ("node_cpu_seconds_total"), d'un ensemble d'étiquettes ("cpu" et "mode") et d'une valeur (0.3).
    - Les étiquettes permettent de segmenter et de filtrer les métriques. Dans cet exemple, elles indiquent que la valeur 0.3 concerne le CPU 0 et le mode "iowait".
- **`<prefix_app>_<nom>_<unit>_<calcul>{<label>="<valeur>", ...} <valeur_metrics>`**:
    - C'est un modèle général pour les noms de métriques Prometheus. Il est recommandé de suivre cette convention pour rendre les métriques plus claires et cohérentes.
    - `<prefix_app>` : un préfixe qui identifie l'application ou le service (par exemple, "node").
    - `<nom>` : le nom de la métrique (par exemple, "cpu_seconds_total").
    - `<unit>` : l'unité de la métrique (par exemple, "seconds").
    - `<calcul>` : le type de calcul (par exemple, "total").
    - `<label>` : les étiquettes qui décrivent les dimensions de la métrique (par exemple, "cpu", "mode").
    - `<valeur_metrics>` : la valeur numérique de la métrique.

---

Prometheus.io est un outil de surveillance et d'alerte open-source puissant, et il peut être extrêmement utile dans plusieurs phases de votre projet d'analyse de données de consommation énergétique des batteries. Voici où et comment vous pourriez l'utiliser :

**1. Collecte et surveillance des données en temps réel :**

- **Phase :** Acquisition des données, exploration et nettoyage des données.
- **Utilisation :**
    - Prometheus est conçu pour collecter des métriques de séries temporelles. Vous pouvez l'utiliser pour surveiller en temps réel les données provenant des capteurs de vos équipements de signalisation (tension, courant, température, etc.).
    - Vous pouvez configurer Prometheus pour extraire régulièrement ces données et les stocker dans sa base de données de séries temporelles.
    - Cela vous permet d'avoir une vue d'ensemble en direct de la consommation énergétique et de l'état des batteries.
    - Prometheus vous permet de surveiller la santé de vos "exporteurs" (logiciels qui vont collecter les données des équipements et les rendre lisibles pour prométhéus).
- **Avantages :**
    - Surveillance continue et en temps réel.
    - Visualisation des données via des tableaux de bord Grafana (qui s'intègrent parfaitement avec Prometheus).
    - Détection rapide des anomalies et des problèmes.

**2. Alertes et notifications :**

- **Phase :** Conception du système d'alerte.
- **Utilisation :**
    - Prometheus vous permet de définir des règles d'alerte basées sur les métriques collectées.
    - Vous pouvez configurer des alertes pour vous avertir lorsque :
        - La tension de la batterie tombe en dessous d'un seuil critique.
        - Le taux de décharge est anormalement élevé.
        - La température de la batterie dépasse une certaine limite.
        - Les valeurs de SOC ou SOH calculées, passent sous un seuil critique.
    - Prometheus peut envoyer des alertes via différents canaux (e-mail, Slack, etc.).
- **Avantages :**
    - Système d'alerte fiable et personnalisable.
    - Réponse rapide aux problèmes potentiels.
    - Prévention des pannes et des situations dangereuses.

**3. Visualisation et analyse des données :**

- **Phase :** Analyse descriptive, validation et évaluation des modèles.
- **Utilisation :**
    - En combinant Prometheus avec Grafana, vous pouvez créer des tableaux de bord personnalisés pour visualiser les données de consommation énergétique et l'état des batteries.
    - Vous pouvez analyser les tendances, identifier les modèles et évaluer les performances de vos modèles d'estimation.
    - Grafana vous permet de créer des graphiques et des visualisations interactives pour faciliter l'analyse des données.
- **Avantages :**
    - Visualisation claire et intuitive des données.
    - Analyse approfondie des tendances et des modèles.
    - Facilitation de la prise de décision.

**En résumé :**

Prometheus.io peut être un outil précieux à plusieurs étapes de votre projet, en particulier pour la collecte, la surveillance, l'alerte et la visualisation des données. Son intégration avec Grafana vous permet de créer un système de surveillance complet et efficace pour la gestion de l'état de santé des batteries de Ver-Mac.


---

