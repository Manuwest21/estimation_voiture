from fastapi import FastAPI, HTTPException, Request, Depends 
from pydantic  import BaseModel
import pandas as pd
from fucntions import simple, predict_car_simple

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello estimation voiture"}





class Donnees(BaseModel):
    marque:str
    modele:str
    chevaux:int
    nbre_portes:int
    
    
@app.post("/quelprix/")
async def prediction(car:Donnees):
    
    prediction=pd.DataFrame(data={ 'nombre_portes': car.marque, 
                                    'chevaux': car.chevaux, 
                                     'marque': car.marque, 
                                    'modele': car.modele,},index=[0])
     
    predire=predict_car_simple(prediction)
     
    return {"predire": predire[0]}
    
    