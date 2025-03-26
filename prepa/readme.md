
### **📢 Pourquoi des alertes ?**  
Imaginons que tu surveilles une tension électrique (voltage). Tu veux être prévenu si :  
✅ **Le voltage dépasse un seuil critique** (ex : > 250V 🔥).  
✅ **Le voltage tombe en dessous d’un minimum** (ex : < 180V ⚠️).  
✅ **Il n’y a plus aucune donnée reçue** (ex : problème de capteur 🛑).  

---

## **⚡ 1. Alerte si le voltage dépasse 250V**
```promql
ALERT HighVoltage
  IF max_voltage > 250
  FOR 2m
  LABELS { severity="critical" }
  ANNOTATIONS {
    summary = "Voltage trop élevé !",
    description = "Le voltage a dépassé 250V depuis 2 minutes."
  }
```
📌 **Explication** :
- L’alerte se déclenche si **`max_voltage` est supérieur à 250V**.  
- Elle doit rester **au-dessus du seuil pendant 2 minutes** avant de s’activer.  
- **Labels** : permet de classer l’alerte (`severity="critical"` pour signaler une urgence).  
- **Annotations** : texte explicatif affiché dans **Grafana** ou une **notification Slack/Email**.  

---

## **⚡ 2. Alerte si le voltage tombe sous 180V**
```promql
ALERT LowVoltage
  IF max_voltage < 180
  FOR 1m
  LABELS { severity="warning" }
  ANNOTATIONS {
    summary = "Voltage trop bas !",
    description = "Le voltage est sous 180V depuis 1 minute."
  }
```
📌 Ici, l’alerte est en **warning** ⚠️ (plutôt qu’en critical) car c’est moins grave.  

---

## **🚨 3. Alerte si aucune donnée reçue depuis 5 minutes**
```promql
ALERT NoVoltageData
  IF absent(max_voltage)
  FOR 5m
  LABELS { severity="critical" }
  ANNOTATIONS {
    summary = "Aucune donnée de voltage reçue !",
    description = "Aucune mise à jour de max_voltage depuis 5 minutes. Capteur ou serveur down ?"
  }
```
📌 Ici, on utilise **`absent()`** pour détecter l’absence de données.  
Si aucune valeur **n’est envoyée depuis 5 minutes**, on déclenche l’alerte.  

---

## **🔗 Déclenchement d’actions avec Alertmanager**
Prometheus tout seul **ne peut pas envoyer d’alerte**. Il faut un **Alertmanager** pour :
✅ Envoyer une notification sur **Slack, Discord, Teams, Telegram, email**  
✅ Déclencher une action automatique  

### **Exemple de règle Alertmanager pour envoyer un email** :
Dans **alertmanager.yml** :
```yaml
receivers:
  - name: "email-alert"
    email_configs:
      - to: "team@hackathon.com"
        from: "alert@monitoring.com"
        smarthost: "smtp.example.com:587"
        auth_username: "alert@monitoring.com"
        auth_password: "yourpassword"
```

---

## **📊 Voir les alertes en live avec Prometheus**
Une fois tes alertes définies, tu peux voir leur état dans Prometheus :  
👉 **Ouvre ton navigateur** et tape :
```
http://localhost:9090/alerts
```
Tu verras une page listant **toutes les alertes actives ou en attente**. 🎯  

---

### **🚀 Résumé pour ton hackathon** :
✅ **Tu définis des règles d’alerte avec PromQL** (ex : voltage trop haut/bas, données manquantes).  
✅ **Tu les relies à Alertmanager** pour envoyer des notifications.  
✅ **Tu peux afficher leur état dans Prometheus** et Grafana.  

