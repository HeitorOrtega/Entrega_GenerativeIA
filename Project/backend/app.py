from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_PATH = "historico_deteccoes.csv"

@app.get("/api/mottu/status")
def get_status():
    df = pd.read_csv(CSV_PATH)
    ultimo = df.dropna(subset=["num_motos_detectadas"]).iloc[-1].to_dict()
    return ultimo
