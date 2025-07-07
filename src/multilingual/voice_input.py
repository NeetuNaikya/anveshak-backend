from whisper import Whisper

class VoiceInput:
    def __init__(self, model_name='base'):
        self.model = Whisper(model_name)

    def transcribe_audio(self, audio_file):
        transcription = self.model.transcribe(audio_file)
        return transcription['text']

    def recognize_command(self, audio_file):
        transcription = self.transcribe_audio(audio_file)
        # Here you can add logic to recognize specific commands or intents from the transcription
        return transcription

# Example usage:
# voice_input = VoiceInput()
# command = voice_input.recognize_command('path_to_audio_file.wav')
# print(command)