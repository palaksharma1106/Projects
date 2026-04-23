import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64

st.set_page_config(page_title="Language Translator", page_icon="🌍")
st.markdown(
    """
    <style>
     .stApp {
        color: black;
    }

    h1 {
        color: black !important;
    }
    .stApp {
        background-image: url("https://i.pinimg.com/1200x/d3/ac/58/d3ac58f05b2108673b5be2f2db43d829.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("🌍 Language Translator")
st.write("Translate text between different languages instantly")

# Language list
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}

# User input
text = st.text_area("Enter text to translate")

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target_lang = st.selectbox("Target Language", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.subheader("Translated Text")
        st.success(translated)

        # Copy button
        st.code(translated)

        # Text to Speech
        tts = gTTS(translated, lang=languages[target_lang])
        tts.save("audio.mp3")

        audio_file = open("audio.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

    else:
        st.warning("Please enter text to translate.")