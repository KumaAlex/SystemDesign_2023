from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Task 1  
    
@app.get("/api")
def getByBinOrIin(bin: str, lang: str):
    try:
        url = f"https://stat.gov.kz/api/juridical?bin={bin}&lang={lang}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        error_msg = "Error making a request to the external API"
        return {"error": error_msg}

# Task 2

class PostInfoReq(BaseModel):
    conditions: list
    cutId: int

@app.post("/api/post")
def postRequest(body: PostInfoReq):
    try:
        url = "https://stat.gov.kz/api/sbr/request?gov"
        response = requests.post(url, json=body.dict())
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        error_msg = "Error making a request to the external API"
        return {"error": error_msg}
    
@app.get("/api/rcut/{lang}")
def getRcutByLang(lang: str):
    try:
        url = f"https://old.stat.gov.kz/api/rcut/${lang}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        error_msg = "Error making a request to the external API"
        return {"error": error_msg}
    
@app.get("/api/check/{num}/{lang}")
def checkRequest(num: str, lang: str):
    try:
        url = f"https://stat.gov.kz/api/sbr/requestResult/{num}/{lang}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        error_msg = "Error making a request to the external API"
        return {"error": error_msg}
    