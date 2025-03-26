### **🛠 Comment configurer Alertmanager simplement ?**  

Alertmanager est un outil qui **prend les alertes envoyées par Prometheus** et les **redirige** vers **email, Discord, Telegram, etc.**.  

---

## **📌 Étape 1 : Créer le fichier `alertmanager.yml`**  
Ce fichier définit **où et comment** envoyer les alertes.  
Voici un exemple basique pour envoyer un email 📧 :  

```yaml
global:
  resolve_timeout: 5m  # Temps avant de considérer une alerte comme résolue

route:
  receiver: "email-alert"  # Nom du canal par défaut pour envoyer les alertes
  group_wait: 30s          # Temps avant d’envoyer la première alerte d’un groupe
  group_interval: 5m       # Temps entre chaque envoi d’alerte du même groupe
  repeat_interval: 1h      # Fréquence de répétition des alertes toujours actives

receivers:
  - name: "email-alert"
    email_configs:
      - to: "ton.email@exemple.com"  # L'adresse qui reçoit les alertes
        from: "alert@monitoring.com" # L'adresse qui envoie les alertes
        smarthost: "smtp.exemple.com:587" # Serveur SMTP pour envoyer l’email
        auth_username: "alert@monitoring.com"
        auth_password: "mot_de_passe"
        require_tls: true  # Active la sécurité TLS
```

---

## **📌 Étape 2 : Démarrer Alertmanager**
1️⃣ Lancer Alertmanager en utilisant le fichier de config :  
```bash
./alertmanager --config.file=alertmanager.yml
```
2️⃣ Aller dans ton navigateur et ouvrir :  
👉 **http://localhost:9093** (pour voir l’interface Alertmanager).  

---

## **📌 Étape 3 : Lier Prometheus à Alertmanager**  
Dans le fichier **prometheus.yml**, ajoute cette ligne pour que **Prometheus envoie les alertes à Alertmanager** :  

```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - "localhost:9093"  # L'adresse où tourne Alertmanager
```

Puis **redémarre Prometheus** :  
```bash
./prometheus --config.file=prometheus.yml
```

---

## **📌 Étape 4 : Tester si Alertmanager fonctionne**
Tu peux simuler une alerte en exécutant :  
```bash
curl -X POST -d '[{"labels":{"alertname":"TestAlerte"}}]' http://localhost:9093/api/v1/alerts
```
Si tout fonctionne, **tu recevras un email** d’alerte ! 🎯  

---

### **🎯 Résumé ultra simple :**
1. **Créer `alertmanager.yml`** et définir **où envoyer les alertes** (email, etc.).  
2. **Démarrer Alertmanager** avec `./alertmanager --config.file=alertmanager.yml`.  
3. **Configurer Prometheus** pour qu’il envoie ses alertes à Alertmanager.  
4. **Tester avec une fausse alerte** et vérifier si tu reçois bien une notification.  

