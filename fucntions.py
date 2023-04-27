import pandas as pd
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer  
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import pandas as pd 
from sklearn.linear_model import LinearRegression, Lasso, Ridge
import seaborn as sns
from sklearn.model_selection import train_test_split
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_car(features):
    X = pd.DataFrame(features, index=[0])
    y_pred = model.predict(X)[0]
    return y_pred