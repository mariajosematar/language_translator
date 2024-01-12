from fastapi import FastAPI, HTTPException
from translation.translator import TranslationService
from pydantic import BaseModel

app = FastAPI()
translator = TranslationService()

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class JeringozaTranslationRequest(BaseModel):
    text: str

@app.post("/translate", response_model=dict)
def translate(request: TranslationRequest):
    try:
        translated_text = translator.translate_text(request.text, request.target_language)
        return {"translation": translated_text, "target_language": request.target_language}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@app.post("/translate/jeringoza", response_model=dict)
def translate_jeringoza(request: JeringozaTranslationRequest):
    try:
        translated_text = translator.translate_to_jeringoza(request.text)
        return {"translation": translated_text}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
