# Voice2Text_Text2Voice
This Streamlit app allows you to record your voice, transcribe it to text, and also convert text to speech — all in one place
Features
🎤 Voice to Text (Speech Recognition)

Uses the audio_recorder_streamlit component to capture audio directly from the browser’s microphone.

Saves the recorded sound to a temporary .wav file.

Uses Python’s SpeechRecognition library with Google Speech Recognition API to transcribe the speech into text.

Displays the transcribed text to the user.

Removes the temporary audio file after processing.

💬 Text to Voice (Speech Synthesis)

Accepts user input as text via a text area.

Uses gTTS (Google Text-to-Speech) to synthesize speech from the entered text.

Saves the generated speech as a temporary .mp3 file.

Plays back the generated audio in the browser.

Warns the user if they try to convert without entering text.

Integration Flow

The user can record a voice clip, see its transcription, then enter text (or reuse the transcribed text) to generate audio output.

All audio processing and playback happens locally in the browser session — no external UI file is needed if running as a single Streamlit script.

Libraries Used

Streamlit → Web application framework

audio-recorder-streamlit → Browser microphone recording

SpeechRecognition → Speech-to-text transcription

gTTS → Text-to-speech generation

tempfile & os → Temporary storage of recorded/generated audio
