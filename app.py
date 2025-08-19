import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

# Page setup
st.set_page_config(page_title="Voice ↔ Text App", layout="centered")
st.title("🎙️ Voice ↔ Text Converter in Streamlit")

st.markdown("This app can **transcribe your voice to text** and **read your text aloud**.")

# ------------------ VOICE → TEXT ------------------
st.header("🎤 Voice to Text")
audio_bytes = audio_recorder(pause_threshold=2.0)  # Adjust sensitivity

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    # Save recorded audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text_output = recognizer.recognize_google(audio_data)
            st.success(f"📝 Transcribed Text: {text_output}")
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Speech recognition service error: {e}")

    os.remove(temp_audio_path)

# ------------------ TEXT → VOICE ------------------
st.header("💬 Text to Voice")
text_input = st.text_area("Enter text to convert into speech:")

if st.button("🔊 Speak"):
    if text_input.strip():
        tts = gTTS(text_input, lang="en")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_tts:
            tts.save(temp_tts.name)
            st.audio(temp_tts.name, format="audio/mp3")
    else:
        st.warning("Please enter some text first.")
