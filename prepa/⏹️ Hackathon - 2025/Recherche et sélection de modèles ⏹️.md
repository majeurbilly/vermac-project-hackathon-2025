État de Charge (SOC - State of Charge) vs État de Santé (SOH - State of Health)
			    Le SOC représente le niveau de charge actuel de la batterie, exprimé en pourcentage de sa capacité totale.
				Le SOH représente la capacité actuelle de la batterie par rapport à sa capacité initiale lorsqu'elle était neuve, également exprimé en pourcentage.


---



**Imaginez une batterie comme un réservoir d'eau :**

- **Le SOC (État de Charge)** :
    - C'est comme savoir combien d'eau il reste dans le réservoir.
    - Si le réservoir est plein, le SOC est de 100 %. S'il est vide, il est de 0 %.
    - Pour le mesurer, on peut regarder le niveau d'eau, ou utiliser des capteurs qui mesurent la pression de l'eau.
- **Le SOH (État de Santé)** :
    - C'est comme savoir si le réservoir est toujours en bon état.
    - Avec le temps, le réservoir peut se fissurer, se rouiller, ou perdre de sa capacité.
    - Le SOH indique à quel point le réservoir est toujours capable de contenir de l'eau par rapport à quand il était neuf.
    - Pour le mesurer, on peut vérifier l'état des parois, ou mesurer la quantité d'eau qu'il peut encore contenir.

**Maintenant, les modèles d'estimation :**

- Ce sont des méthodes pour deviner le SOC et le SOH sans avoir à vider le réservoir ou à l'ouvrir.
- **Modèles basés sur la tension :**
    - C'est comme deviner combien d'eau il reste en regardant la pression.
    - Plus la pression est élevée, plus il y a d'eau.
- **Modèles basés sur le comptage de Coulomb :**
    - C'est comme compter combien d'eau on a ajouté ou enlevé du réservoir.
    - On utilise des capteurs pour mesurer le débit d'eau.
- **Modèles d'apprentissage automatique :**
    - C'est comme utiliser un ordinateur pour apprendre à deviner le SOC et le SOH à partir de nombreuses données.
    - L'ordinateur apprend à reconnaître les motifs et les tendances.

**Comment faire concrètement :**

1. **Collecter des données :**
    - Obtenir des données de capteurs qui mesurent la tension, le courant et la température des batteries.
2. **Choisir un modèle :**
    - Décider quelle méthode est la plus adaptée aux données disponibles et aux besoins du projet.
3. **Entraîner le modèle :**
    - Utiliser les données collectées pour apprendre au modèle à faire des prédictions précises.
4. **Tester le modèle :**
    - Vérifier si le modèle fait de bonnes prédictions en le comparant à des données réelles.
5. **Ajuster le modèle :**
    - Modifier les paramètres du modèle pour améliorer sa précision.

**En résumé :**

- L'étude des modèles d'estimation consiste à apprendre à utiliser différentes méthodes pour deviner l'état de santé des batteries.
- C'est comme apprendre à lire les signes vitaux d'une batterie pour savoir si elle est en bonne santé.

