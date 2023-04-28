import streamlit as st
import pandas as pd
import pandas as pd
import pickle
import joblib
from fucntions import predict_car, predict_car_simple, recherche
# def load_model():
#     with open('model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     return model


# def predict_car(features):
#     X = pd.DataFrame(features, index=[0])
#     model = load_model()
#     y_pred = model.predict(X)
#     return y_pred
# predire=model.predict_car(prediction)
#         # result = predict_car(prediction)
#         st.write(predire)

# model=joblib.load('price_car.joblib')

df = pd.read_csv('voiture_final.csv')

st.title("à vous pour estimer le prix de votre voiture!")
# Créer la liste des marques

marques = df['marque'].unique().tolist()
modele = df["modele"].unique().tolist()
etat_route = df['etat_de_route'].unique().tolist()
nombre_portes = df['nombre_portes'].unique().tolist()
empattement = df['empattement'].unique().tolist()
longueur = df['longueur_voiture'].unique().tolist()
largeur= df['largeur_voiture'].unique().tolist()
hauteur = df['hauteur_voiture'].unique().tolist()
chevaux = df['chevaux'].unique().tolist()
poids = df['poids_vehicule'].unique().tolist()#
nombre_cylindres = df['nombre_cylindres'].unique().tolist()
moteur_cc3 = df['moteur_cc3'].unique().tolist()
taux_alésage = df['taux_alésage'].unique().tolist()
taux_compression = df['taux_compression'].unique().tolist()
tour_moteur = df['tour_moteur'].unique().tolist()
conso_ville = df['consommation_ville'].unique().tolist()
conso_autoroute = df['consommation_autoroute'].unique().tolist()
carburant = df['carburant'].unique().tolist()#
turbo = df['turbo'].unique().tolist()#
type_vehicule = df['type_vehicule'].unique().tolist()
roues_motrices = df['roues_motrices'].unique().tolist()
emplacement_moteur = df['emplacement_moteur'].unique().tolist()
type_moteur = df['type_moteur'].unique().tolist()
systeme_carburant = df['systeme_carburant'].unique().tolist()
course = df['course'].unique().tolist()



st.markdown("<span style='color:green'>Rentrez les détails du véhicule</span>", unsafe_allow_html=True)

    
    # Propose de chercher un film ou une série
# choix = st.radio("Rechercher un/e", options=["Estimation simple", "Estimation approfondie"])
# if choix=="Estimation simple":
marque = st.selectbox('Sélectionnez une marque', marques)
modele = st.selectbox('Sélectionnez un modéle', modele)
chevaux= st.slider("combien de chevaux :", 40, 130)
nombre_portes = st.selectbox('combien de portes', nombre_portes)

prediction=pd.DataFrame(data={ 'nombre_portes': nombre_portes, 
                'chevaux': chevaux, 
                'marque': marque, 
                'modele': modele},index=[0])


if st.button('Estimer'):
    predire=predict_car_simple(prediction)
    st.write(f"la predictione est de {predire}")