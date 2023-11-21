import moviepy.editor as mp
import speech_recognition as sr

# Function to transcribe an MP4 file to text
def transcribe_mp4_to_text(mp4_path, output_text_file):
    print("Loading the MP4 video...")
    video_clip = mp.VideoFileClip(mp4_path)
    print("Video loaded.")

    print("Extracting audio from the video...")
    audio_clip = video_clip.audio
    print("Audio extracted.")

    print("Saving the extracted audio as a WAV file...")
    audio_wav_path = "temp_audio.wav"
    audio_clip.write_audiofile(audio_wav_path)
    print("Audio saved as WAV.")

if __name__ == "__main__":
    mp4_file_path = input("Enter the path to your input MP4 file: ")
    output_text_file_path = input("Enter the path to the output transcript file: ")

    transcribe_mp4_to_text(mp4_file_path, output_text_file_path)
