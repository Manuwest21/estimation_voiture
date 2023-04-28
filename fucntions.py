import pandas as pd
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer  
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import pandas as pd 
from sklearn.linear_model import LinearRegression, Lasso, Ridge

from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd

df = pd.read_csv('voiture_final.csv')
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
def tous():
    with open('model_poly.pkl', 'rb') as file:
        model = pickle.load(file)
        return model
    
def simple():
    with open('model_simple.pkl', 'rb') as file:
        model = pickle.load(file)
        return model
    
def ss_modele():
    with open('sans_modele.pkl', 'rb') as file:
        model = pickle.load(file)
        return model
    

def predict_car(features):
    X = pd.DataFrame(features, index=[0])
    model=tous()
    y_pred = model.predict(X)[0]
    return y_pred


def predict_car_simple(features):
    X = pd.DataFrame(features, index=[0])
    model=simple()
    y_pred = model.predict(X)[0]
    return y_pred

def predict_ss_modele(features):
    X = pd.DataFrame(features, index=[0])
    model=ss_modele()
    y_pred = model.predict(X)[0]
    return y_pred



def recherche():
    st.title("Recherche de films et séries")
    
    # Propose de chercher un film ou une série
    choix = st.radio("Rechercher un/e", options=["Estimation simple", "Estimation approfondie"])
    if choix=="Estimation simple":
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
        
    if choix=="Estimation approfondie":
        

        
# Afficher la liste déroulante pour sélectionner une marque

        marque = st.selectbox('Sélectionnez une marque', marques)
        modele = st.selectbox('Sélectionnez un modéle', modele)
        nombre_portes = st.selectbox('combien de portes', nombre_portes)
        empattement = st.slider('Sélectionnez l\'empattement', 1.0, 6.0,0.1)
        longueur = st.slider("renseignez la longueur:", 1.00, 3.00,0.01)
        largeur= st.slider("renseignez la largeur:", 1.00, 4.00,0.01)
        etat_de_route = st.selectbox('Sélectionnez un etat de route', etat_route)
        hauteur= st.slider("renseignez la largeur:", 4.00, 5.00,0.01)
        nombre_cylindres = st.slider("rentrez le nombre de cylindres :", 2, 12)
        taux_alésage= st.slider("quel taux alésage:", 2.30, 3.80,0.01)
        taux_compression= st.slider("combien de taux compression :", 8.0, 25.0,0.1)
        chevaux= st.slider("combien de chevaux :", 40, 130)
        course= st.slider("quel taux alésage:", 2.30, 3.70,0.01)
        tour_moteur = st.slider("Entrez une valeur entre 3500 et 7000 :", 3500, 7000)
        consommation_ville= st.slider("consommation du vehicule en ville :", 3.0, 16.0,0.1)
        consommation_autoroute = st.slider("consommation du vehicule sur autoroute :", 3.0, 16.0,0.1)
        poids = st.slider("renseignez le poids:", 1.0, 3.0,0.1)
        carburant = st.selectbox('Sélectionnez le carburant', carburant)
        turbo = st.selectbox("Sélectionnez s'il existe un turbo", turbo)
        type_vehicule = st.selectbox("Sélectionnez le type de véhicule", type_vehicule)
        systeme_carburant= st.selectbox('Sélectionnez le systeme de carburant', systeme_carburant)
        moteur_cc3 = st.slider("Entrez le moteur cc3 :", 1000, 5000)
        type_moteur = st.selectbox("quel type moteur", type_moteur)
        emplacement_moteur = st.selectbox("ou est emplacement moteur", emplacement_moteur)
        roues_motrices = st.selectbox('combien de roues motrices', roues_motrices)


        prediction=pd.DataFrame(data={'etat_de_route': etat_de_route, 'nombre_portes': nombre_portes, 
                        'empattement': empattement, 'longueur_voiture': longueur, 
                        'largeur_voiture': largeur, 'hauteur_voiture': hauteur, 
                        'poids_vehicule': poids, 'nombre_cylindres': nombre_cylindres, 
                        'moteur_cc3': moteur_cc3, 'taux_alésage': taux_alésage,  
                        'taux_compression': taux_compression, 'chevaux': chevaux, 
                        'tour_moteur': tour_moteur, 'consommation_ville': consommation_ville, 
                        'consommation_autoroute': consommation_autoroute, 'marque': marque, 
                        'modele': modele, 'carburant': carburant, 'turbo': turbo, 
                        'type_vehicule': type_vehicule, 'roues_motrices': roues_motrices, 
                        'emplacement_moteur': emplacement_moteur, 'type_moteur': type_moteur, 
                        'systeme_carburant': systeme_carburant,"course":course},index=[0])





        if st.button('Estimer'):
            prediction=pd.DataFrame(data={'etat_de_route': etat_de_route, 'nombre_portes': nombre_portes, 
                            'empattement': empattement, 'longueur_voiture': longueur, 
                            'largeur_voiture': largeur, 'hauteur_voiture': hauteur, 
                            'poids_vehicule': poids, 'nombre_cylindres': nombre_cylindres, 
                            'moteur_cc3': moteur_cc3, 'taux_alésage': taux_alésage,  
                            'taux_compression': taux_compression, 'chevaux': chevaux, 
                            'tour_moteur': tour_moteur, 'consommation_ville': consommation_ville, 
                            'consommation_autoroute': consommation_autoroute, 'marque': marque, 
                            'modele': modele, 'carburant': carburant, 'turbo': turbo, 
                            'type_vehicule': type_vehicule, 'roues_motrices': roues_motrices, 
                            'emplacement_moteur': emplacement_moteur, 'type_moteur': type_moteur, 
                            'systeme_carburant': systeme_carburant,"course":course},index=[0])
        
        
        
            predire=predict_car(prediction)
            # result = predict_car(prediction)
            st.write(f"la predictione est de {predire}")
            
    else:
        st.title('here')
        