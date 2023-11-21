import whisper

def transcribe_audio(audio_file_path):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    try:
        result = model.transcribe(audio_file_path, verbose=True)
        transcription = result["text"]
        return transcription
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

audio_file_path = 'temp_audio.wav'

# Transcribe the audio
transcription = transcribe_audio(audio_file_path)

if transcription:
    print("Transcription:")
    print(transcription)
else:
    print("Failed to transcribe the audio.")
