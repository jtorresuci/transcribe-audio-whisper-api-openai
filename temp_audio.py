import moviepy.editor as mp
import speech_recognition as sr

# Function to transcribe an MP4 file to text
def transcribe_mp4_to_text(mp4_path, output_text_file):
    # Load the MP4 video
    video_clip = mp.VideoFileClip(mp4_path)

    # Extract audio from the video
    audio_clip = video_clip.audio

    # Save the extracted audio as a WAV file
    audio_wav_path = "temp_audio.wav"
    audio_clip.write_audiofile(audio_wav_path)

    

if __name__ == "__main__":
    mp4_file_path = input("Enter file name: ")
    output_text_file_path = "output_transcript.txt"

    transcribe_mp4_to_text(mp4_file_path, output_text_file_path)
