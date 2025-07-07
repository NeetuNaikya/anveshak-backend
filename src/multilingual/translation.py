from googletrans import Translator

class TranslationService:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, target_language):
        try:
            translated = self.translator.translate(text, dest=target_language)
            return translated.text
        except Exception as e:
            print(f"Error during translation: {e}")
            return text

    def detect_language(self, text):
        try:
            detected = self.translator.detect(text)
            return detected.lang
        except Exception as e:
            print(f"Error during language detection: {e}")
            return None

# Example usage
if __name__ == "__main__":
    translation_service = TranslationService()
    text_to_translate = "Hello, how can I help you?"
    translated_text = translation_service.translate_text(text_to_translate, 'hi')
    print(f"Translated text: {translated_text}")