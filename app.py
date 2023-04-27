import streamlit as st
import pandas as pd
# from fucntions import predict_car
import pandas as pd
import pickle
import joblib
# from sklearn.model_selection import GridSearchCV
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.compose import ColumnTransformer  
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline
# import pandas as pd 
# from sklearn.linear_model import LinearRegression, Lasso, Ridge
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# Charger les données

# def load_model():
#     with open('model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     return model


# def predict_car(features):
#     X = pd.DataFrame(features, index=[0])
#     model = load_model()
#     y_pred = model.predict(X)
#     return y_pred


model=joblib.load('price_car.joblib')

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




# Afficher la liste déroulante pour sélectionner une marque
marque = st.selectbox('Sélectionnez une marque', marques)
modele = st.selectbox('Sélectionnez un modéle', modele)
nombre_portes = st.selectbox('combien de portes', nombre_portes)
empattement= st.selectbox('on est sur quel empattement', empattement)
longueur = st.selectbox('la longueur?', longueur)
largeur= st.selectbox('Sélectionnez la largeur', largeur)
etat_de_route = st.selectbox('Sélectionnez un modéle', etat_route)
hauteur= st.selectbox('Sélectionnez un modéle', hauteur)
nombre_cylindres = st.selectbox('Sélectionnez un modéle', nombre_cylindres)
taux_alésage= st.selectbox('Sélectionnez un modéle', taux_alésage)
taux_compression= st.selectbox('combien de taux compression?', taux_compression)
chevaux= st.selectbox('combien de chevaux', chevaux)
course= st.selectbox('combien de course', course)
tour_moteur = st.slider("Entrez une valeur entre 3500 et 7000 :", 3500, 7000)
consommation_ville= st.slider("consommation du vehicule en ville :", 3, 16)
consommation_autoroute = st.slider("consommation du vehicule sur autoroute :", 3, 16)
poids = st.slider("renseignez le poids:", 1, 2)
carburant = st.selectbox('Sélectionnez le carburant', carburant)
turbo = st.selectbox("Sélectionnez s'il existe un turbo", turbo)
type_vehicule = st.selectbox("Sélectionnez le type de véhicule", type_vehicule)
systeme_carburant= st.selectbox('Sélectionnez le systeme de carburant', systeme_carburant)
moteur_cc3 = st.selectbox("Sélectionnez s'il existe un turbo", type_moteur)
type_moteur = st.selectbox("Sélectionnez s'il existe un turbo", moteur_cc3)
emplacement_moteur = st.selectbox("Sélectionnez s'il existe un turbo", emplacement_moteur)
roues_motrices = st.selectbox('Sélectionnez roues motrices', roues_motrices)
# selection_modele = st.selectbox('Sélectionnez un modéle', modele)
# selection_marque = st.selectbox('Sélectionnez une marque', marques)
# selection_modele = st.selectbox('Sélectionnez un modéle', modele)
# selection_marque = st.selectbox('Sélectionnez une marque', marques)
# selection_modele = st.selectbox('Sélectionnez un modéle', modele)
# selection_marque = st.selectbox('Sélectionnez une marque', marques)
# selection_modele = st.selectbox('Sélectionnez un modéle', modele)
# selection_marque = st.selectbox('Sélectionnez une marque', marques)
# selection_modele = st.selectbox('Sélectionnez un modéle', modele)
# selection_marque = st.selectbox('Sélectionnez une marque', marques)
# selection_modele = st.selectbox('Sélectionnez un modéle', modele)
# # Filtrer les données en fonction de la marque sélectionnée
# filtered_df = df[df['marque'] == selection_marque]

# Afficher les données filtrées
# st.write(filtered_df)

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





if st.button('Prédire'):
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
    
    
    predire=model.predict(prediction)
    # result = predict_car(prediction)
    st.write('predire')
    
    
    
