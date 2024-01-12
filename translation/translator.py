from googletrans import Translator

class TranslationService:
    SUPPORTED_LANGUAGES = {"es": "Spanish", "de": "German", "fr": "French", "it": "Italian", "da": "Danish"}

    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text: str, target_language: str) -> str:
        target_language = target_language.lower()

        if target_language not in self.SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {target_language}")

        translated_text = self.translator.translate(text, dest=target_language).text
        return translated_text

    def translate_to_jeringoza(self, text: str) -> str:
        # Implementa la lógica de traducción a Jeringoza según los requisitos
        translated_text = text[::-1]
        return translated_text