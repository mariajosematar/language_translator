from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class JeringozaTranslationRequest(BaseModel):
    text: str

def translate_text(text: str, target_language: str) -> str:
    # lógica real para traducir el texto al idioma especificado
    translated_text = f"Translation of '{text}' to {target_language} goes here"
    return translated_text

def translate_to_jeringoza(text: str) -> str:
    # lógica real para traducir el texto a Jeringoza
    translated_text = f"Jeringoza translation of '{text}' goes here"
    return translated_text

@app.post("/translate", response_model=dict)
def translate(request: TranslationRequest):
    supported_languages = ["Spanish", "German", "French", "Italian", "Danish"]
    
    if request.target_language.capitalize() not in supported_languages:
        raise HTTPException(status_code=400, detail="Unsupported language")

    translated_text = translate_text(request.text, request.target_language.capitalize())
    return {"translation": translated_text, "target_language": request.target_language}

@app.post("/translate/jeringoza", response_model=dict)
def translate_jeringoza(request: JeringozaTranslationRequest):
    translated_text = translate_to_jeringoza(request.text)
    return {"translation": translated_text}