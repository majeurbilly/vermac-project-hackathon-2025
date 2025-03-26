from prometheus_client import start_http_server, Gauge
import time
import json

def extraire_donnees_logs(chemin_fichier):
    """
    Extrait les données de log du fichier JSON avec timestamps.
    """
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)

        logs = donnees[0]['Logs']
        donnees_extraites = {}

        for log in logs:
            nom_metrique = log['Name'].replace(" ", "_").replace("-", "_").lower()
            if log['Values']:
                derniere_valeur = log['Values'][-1]  # Dernière valeur avec timestamp
                if isinstance(derniere_valeur, dict) and 'V' in derniere_valeur and 'T' in derniere_valeur:
                    valeur = derniere_valeur['V']
                    timestamp = derniere_valeur['T']
                    if nom_metrique == "position":
                        donnees_extraites["latitude_value"] = {"valeur": valeur[0], "timestamp": timestamp}
                        donnees_extraites["longitude_value"] = {"valeur": valeur[1], "timestamp": timestamp}
                    else:
                        donnees_extraites[f"{nom_metrique}_value"] = {"valeur": valeur, "timestamp": timestamp}
                else:
                    print(f"Erreur : Structure de données incorrecte pour {nom_metrique}")
                    print(f"Dernière valeur : {derniere_valeur}")
                    # Gérer l'erreur ou ignorer cette métrique
            else:
                print(f"Erreur : Aucune valeur trouvée pour {nom_metrique}")

        return donnees_extraites

    except FileNotFoundError:
        print(f"Erreur : Le fichier {chemin_fichier} est introuvable.")
        return {}
    except json.JSONDecodeError:
        print(f"Erreur : JSON invalide dans {chemin_fichier}.")
        return {}
    except KeyError:
        print("Erreur : Structure du fichier incorrecte.")
        return {}

if __name__ == '__main__':
    start_http_server(8000)
    print("Serveur Prometheus démarré sur le port 8000")

    gauges = {}  # Stocker les métriques Gauge
    uptime_valeurs = {}  # Stocker les valeurs précédentes de uptime

    while True:
        donnees_logs = extraire_donnees_logs("./data/PCMS_001.json")
        for nom_metrique, data in donnees_logs.items():
            if data:  # Vérifier si data n'est pas vide
                valeur = data['valeur']
                timestamp = data['timestamp']

                # Créer ou mettre à jour la métrique Gauge avec un label pour le timestamp
                if nom_metrique not in gauges:
                    gauges[nom_metrique] = Gauge(nom_metrique, f"Valeur de {nom_metrique}", ["timestamp"])

                try:
                    gauges[nom_metrique].labels(timestamp=timestamp).set(float(valeur))
                    print(f"Mise à jour de {nom_metrique} avec {valeur} (timestamp: {timestamp})")

                    # Gestion spécifique de uptime
                    if nom_metrique == "uptime_value":
                        if "uptime_value" in uptime_valeurs:
                            uptime_valeurs["uptime_previous_value"] = uptime_valeurs["uptime_last_value"]
                        uptime_valeurs["uptime_last_value"] = float(valeur)

                        # Créer ou mettre à jour les métriques uptime_last_value et uptime_previous_value
                        if "uptime_last_value" in uptime_valeurs:
                            if "uptime_last_value" not in gauges:
                                gauges["uptime_last_value"] = Gauge("uptime_last_value", "Dernière valeur de uptime")
                            gauges["uptime_last_value"].set(uptime_valeurs["uptime_last_value"])

                        if "uptime_previous_value" in uptime_valeurs:
                            if "uptime_previous_value" not in gauges:
                                gauges["uptime_previous_value"] = Gauge("uptime_previous_value", "Valeur précédente de uptime")
                            gauges["uptime_previous_value"].set(uptime_valeurs["uptime_previous_value"])

                except (ValueError, TypeError):
                    print(f"Erreur : Impossible de convertir la valeur en float pour {nom_metrique}")
                    print(f"Valeur : {valeur}")
            else:
                print(f"Erreur : Données manquantes pour {nom_metrique}")
        time.sleep(10)