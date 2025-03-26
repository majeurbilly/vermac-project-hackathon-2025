---
weeks_at_school: 24
days_at_school: 174
tags:
---
![[Pasted image 20250324000128.png]]

batterie < installer un runner du style micropython pour roulé un programme qui exporte les donnée sur ... un port ¯\_(ツ)_/¯

batterie < serveur web qui roule un boucle en executant des fonction pour aller chercher le file dans la batterie(file qui comporte le % par exemple) et puis crie ce qui catch sur son port

serveur web > port x < prometheus lui ecoute tout les ports autour de lui([[config host on docker]]) et si y a des metric il les ramasse et créé une table pour elles

prometheus < grafana collecte les donnée de la table de prometheus vis sa config et en fait de graphique 


tat de donnée (3 valeurs - courant utilisé -  courant max - courant changé) 
chaque jour des data tombe 
prédire le jours suivant le plus proche mais aprochimatif

promQL

trouvé la data > la put metric exporter > prom > requete promql > config alert
https://prometheus.github.io/client_python/
https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
https://logz.io/blog/promql-examples-introduction/#prometheustypes
https://prometheus.io/docs/prometheus/latest/querying/examples/