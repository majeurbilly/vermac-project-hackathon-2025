from prometheus_client import start_http_server, Gauge
import time
import json

# Variables globales pour conserver les valeurs
metrics_values = {
    "voltage_battery_value": None,
    "voltage_solar_value": None,
    "current_battery_value": None,
    "current_solar_value": None,
    "uptime_value": None,
    "uptime_last_value": None,
    "latitude_value": None,
    "longitude_value": None,
    "current_battery_charge": 420
}
INITIAL_CAPACITY = 420

# Créer un Gauge pour le SOH
soh_gauge = Gauge('battery_soh', 'State of Health (SOH) de la batterie')

def calculer_soh(current_capacity):
    """
    Calcule l'état de santé (SOH) de la batterie en fonction de la capacité actuelle.
    """
    soh = (current_capacity / INITIAL_CAPACITY) * 100
    return soh

def calculer_current_capacity():
    """
    Calcule la capacité actuelle de la batterie en fonction des valeurs solaires et de la batterie.
    """
    if metrics_values["voltage_solar_value"] is not None and metrics_values["current_solar_value"] is not None and \
            metrics_values["voltage_battery_value"] is not None and metrics_values["current_battery_value"] is not None:
        current_charge_change = (metrics_values["voltage_solar_value"] * metrics_values["current_solar_value"]) - (
                    metrics_values["voltage_battery_value"] * metrics_values["current_battery_value"])
        metrics_values["current_battery_charge"] = metrics_values["current_battery_charge"] + current_charge_change if \
        metrics_values["current_battery_charge"] else current_charge_change

        # Si la capacité actuelle dépasse la capacité initiale, on la fixe à la capacité initiale
        if metrics_values["current_battery_charge"] > INITIAL_CAPACITY:
            metrics_values["current_battery_charge"] = INITIAL_CAPACITY

    return metrics_values["current_battery_charge"]

def extraire_donnees_logs(chemin_fichier):
    """
    Extrait les données de log du fichier JSON avec timestamps et met à jour metrics_values.
    """
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)

        logs = donnees[0]['Logs']

        # Itérer sur chaque log pour extraire les valeurs et mettre à jour metrics_values
        for log in logs:
            nom_metrique = log['Name'].replace(" ", "_").replace("-", "_").lower()

            if log['Values']:
                for derniere_valeur in log['Values']:
                    if isinstance(derniere_valeur, dict) and 'V' in derniere_valeur and 'T' in derniere_valeur:
                        valeur = derniere_valeur['V']
                        timestamp = derniere_valeur['T']

                        # Mise à jour de metrics_values pour les différentes métriques
                        if nom_metrique == "position":
                            metrics_values["latitude_value"] = valeur[0]
                            metrics_values["longitude_value"] = valeur[1]
                        else:
                            # Pour les autres métriques (ex: voltage, current, etc.)
                            if nom_metrique == "voltage_battery":
                                metrics_values["voltage_battery_value"] = valeur
                            elif nom_metrique == "voltage_solar":
                                metrics_values["voltage_solar_value"] = valeur
                            elif nom_metrique == "current_battery":
                                metrics_values["current_battery_value"] = valeur
                            elif nom_metrique == "current_solar":
                                metrics_values["current_solar_value"] = valeur
                            elif nom_metrique == "uptime":
                                metrics_values["uptime_value"] = valeur

                    else:
                        print(f"Erreur : Structure de données incorrecte pour {nom_metrique}")
                        print(f"Dernière valeur : {derniere_valeur}")
            else:
                print(f"Erreur : Aucune valeur trouvée pour {nom_metrique}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {chemin_fichier} est introuvable.")
    except json.JSONDecodeError:
        print(f"Erreur : JSON invalide dans {chemin_fichier}.")
    except KeyError:
        print("Erreur : Structure du fichier incorrecte.")


if __name__ == '__main__':
    start_http_server(8000)
    print("Serveur Prometheus démarré sur le port 8000")

    gauges = {}  # Stocker les métriques Gauge
    uptime_valeurs = {}  # Stocker les valeurs précédentes de uptime

    while True:
        # Extraire les données du fichier JSON et mettre à jour metrics_values
        extraire_donnees_logs("./Dataset/wetransfer/data/PCMS_008.json")

        # Mise à jour de la métrique pour chaque valeur de metrics_values
        for nom_metrique, valeur in metrics_values.items():
            if valeur is not None:  # Si la valeur existe, on la met à jour
                if nom_metrique not in gauges:
                    gauges[nom_metrique] = Gauge(nom_metrique, f"Valeur de {nom_metrique}")

                try:
                    gauges[nom_metrique].set(float(valeur))  # Mettre à jour la métrique avec la valeur

                    print(f"Mise à jour de {nom_metrique} avec {valeur}")

                except (ValueError, TypeError):
                    print(f"Erreur : Impossible de convertir la valeur en float pour {nom_metrique}")
                    print(f"Valeur : {valeur}")

        # Appeler calculer_current_capacity à chaque itération
        calculer_current_capacity()

        # Calculer et afficher le SOH
        if metrics_values["current_battery_charge"] is not None:
            soh = calculer_soh(metrics_values["current_battery_charge"])
            # Arrondir le SOH à 4 décimales
            soh_rounded = round(soh, 4)
            print(f"SOH: {soh_rounded}%")

            # Mettre à jour le Gauge du SOH avec la valeur arrondie
            soh_gauge.set(soh_rounded)

        time.sleep(10)
