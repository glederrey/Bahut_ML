# Datasets

Vous avez deux jeux de données mis à disposition par votre employeur. 

## Passenger satisfaction

Il s'agit d'un dataset de classification dont l'objectif est de prédire si les passagers d'une compagnie aérienne sont satisfaits ou non de leur vol. Le dataset contient des données d'enquête de satisfaction des passagers avec différentes métriques permettant d'évaluer leur expérience.

Variables
- ID: ID du passager
- Gender: Genre du passager (Female, Male)
- Customer Type: Type de client (Loyal customer, disloyal customer)
- Age: Âge du passager
- Type of Travel: Motif du voyage (Personal Travel, Business Travel)
- Class: Classe de voyage (Business, Eco, Eco Plus)
- Flight distance: Distance du vol
- Inflight wifi service: Niveau de satisfaction du service wifi à bord (0:Non Applicable;1-5)
- Departure/Arrival time convenient: Niveau de satisfaction des horaires de départ/arrivée
- Ease of Online booking: Niveau de satisfaction de la réservation en ligne
- Gate location: Niveau de satisfaction de l'emplacement de la porte d'embarquement
- Food and drink: Niveau de satisfaction de la restauration
- Online boarding: Niveau de satisfaction de l'embarquement en ligne
- Seat comfort: Niveau de satisfaction du confort du siège
- Inflight entertainment: Niveau de satisfaction du divertissement en vol
- On-board service: Niveau de satisfaction du service à bord
- Leg room service: Niveau de satisfaction de l'espace pour les jambes
- Baggage handling: Niveau de satisfaction de la gestion des bagages
- Checkin service: Niveau de satisfaction du service d'enregistrement
- Inflight service: Niveau de satisfaction du service en vol
- Cleanliness: Niveau de satisfaction de la propreté
- Departure Delay in Minutes: Minutes de retard au départ
- Arrival Delay in Minutes: Minutes de retard à l'arrivée
- Satisfaction: Niveau de satisfaction global (Satisfaction, neutral or dissatisfaction)

## Flight prices

Il s'agit d'un dataset de régression dont l'objectif est de prédire le prix d'un billet d'avion en fonction de différentes caractéristiques du vol. Le dataset contient des données de vols entre les aéroports suivants :

["ORD", "LAX", "JFK", "LAS", "BOS", "SFO"]

Les données ont été collectées sur plusieurs jours de recherche, avec pour chaque jour des informations sur différents vols.

Variables :
- Searched Date : Date à laquelle le vol a été recherché
- Departure Date : Date et heure de départ du vol
- Arrival Date : Date et heure d'arrivée du vol
- Flight Lands Next Day : Booléen indiquant si le vol arrive le lendemain du départ
- Departure Airport : Aéroport de départ
- Arrival Airport : Aéroport d'arrivée  
- Number Of Stops : Nombre d'escales
- Route : Détail des escales du vol
- Airline : Compagnie aérienne
- Cabin : Classe de voyage (Economy, Business, etc.)
- Price : Prix du billet (variable cible)
