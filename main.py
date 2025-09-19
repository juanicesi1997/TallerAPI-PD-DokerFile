import joblib as jl
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class customerData(BaseModel):
    tenure: float
    usage_frequency: float
    support_calls: float
    payment_delay: float
    subscription_type: str
    contract_length: str
    total_spend: float
    last_interaction: float

model_path = 'models/model.joblib'
app = FastAPI()

model = jl.load(model_path)

@app.post("/")
def welcome():
    print("Welcome")

@app.post("/predict/")
def model_prediction(payload: customerData):
    print(payload.model_dump())
    df = pd.DataFrame.from_dict(payload.model_dump(), orient='index').T
    print(df)
    df['subscription_type'] = df['subscription_type'].astype('category')
    df['contract_length'] = df['contract_length'].astype('category')
    df['tenure'] = df['tenure'].astype('float')
    df['usage_frequency'] = df['usage_frequency'].astype('float')
    df['support_calls'] = df['support_calls'].astype('float')
    df['payment_delay'] = df['payment_delay'].astype('float')
    df['total_spend'] = df['total_spend'].astype('float')
    df['last_interaction'] = df['last_interaction'].astype('float')    
    prediction = model.predict(df)
    
    return {'prediccion': prediction.item() }
